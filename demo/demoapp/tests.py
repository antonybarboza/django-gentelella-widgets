import json

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.template import Template, Context
from selenium.webdriver.chrome.webdriver import WebDriver

from django import forms
from django.test import TestCase, RequestFactory
from django.urls import reverse, reverse_lazy

from rest_framework import status, serializers
from selenium.webdriver.common.by import By

from djgentelella.views.storymap import BaseStoryMapMBView, BaseStoryMapGPView
from djgentelella.widgets.storymap import MapBasedStoryMapInput, GigaPixelStoryMapInput


class StoryMapWithSeleniumTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver(executable_path='/Users/mariovargas/Desktop/chromedriver')
        cls.selenium.implicitly_wait(10)
        super(StoryMapWithSeleniumTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(StoryMapWithSeleniumTestCase, cls).tearDownClass()
        cls.selenium.quit()

    def test_display_storymaps(self):
        self.selenium.get(self.live_server_url)
        # Find storymap obj
        assert 'mapbased_storymap' in self.selenium.page_source
        assert 'gigapixel_storymap' in self.selenium.page_source

    def test_slides_title_data(self):
        self.selenium.get(self.live_server_url)

        response = self.selenium.find_element(By.CSS_SELECTOR, 'body').text
        self.assertTrue('COSTA RICA PLACES TO VISIT' in response)
        self.assertTrue('A Sunday on La Grande Jatte' in response)


class StoryMapFormWidgetTest(TestCase):

    def setUp(self):
        class StoryMapFormClass(forms.Form):
            gp_storymap = forms.CharField(widget=GigaPixelStoryMapInput, required=False)
            mb_storymap = forms.CharField(widget=MapBasedStoryMapInput, disabled=True)

        self.form = StoryMapFormClass()

    def render(self, msg, context={}):
        template = Template(msg)
        context = Context(context)
        return template.render(context)

    def test_widget_id_form(self):
        gp_storymap_id = self.render('{{form.gp_storymap.id_for_label}}', {'form': self.form})
        mb_storymap_id = self.render('{{form.mb_storymap.id_for_label}}', {'form': self.form})
        self.assertEqual(gp_storymap_id, 'id_gp_storymap')
        self.assertEqual(mb_storymap_id, 'id_mb_storymap')

    def test_widget_name_form(self):
        gp_storymap_name = self.render('{{form.gp_storymap.html_name}}', {'form': self.form})
        mb_storymap_name = self.render('{{form.mb_storymap.html_name}}', {'form': self.form})
        self.assertEqual(gp_storymap_name, 'gp_storymap')
        self.assertEqual(mb_storymap_name, 'mb_storymap')

    def test_form_field_id(self):
        storymap = self.render('{{form}}', {'form': self.form})
        self.assertIn('id="id_gp_storymap"', storymap)
        self.assertIn('id="id_mb_storymap"', storymap)

    def test_form_field_data_widget(self):
        storymap = self.render('{{form}}', {'form': self.form})
        self.assertIn('data-widget="GigaPixelStoryMapInput"', storymap)
        self.assertIn('data-widget="MapBasedStoryMapInput"', storymap)

    def test_widget_required_false(self):
        required = self.render('{{form.gp_storymap.required}}', {'form': self.form})
        self.assertFalse(required)

    def test_widget_disabled_true(self):
        disabled = self.render('{{form.mb_storymap.disabled}}', {'form': self.form})
        self.assertFalse(disabled)


class MapBasedStoryMapWidgetTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.mapbased_view = BaseStoryMapMBView()
        self.storymap = forms.CharField(widget=MapBasedStoryMapInput(
            attrs={"data-url": reverse_lazy('examplestorymapmb-list')}))

        self.url = reverse('examplestorymapmb-list')

    def test_assert_response_valid_data(self):
        request = self.factory.get(self.url)
        response = self.mapbased_view.list(request)

        self.assertEqual(response.status_code, 200)

    def test_assert_response_invalid_data(self):
        request = self.factory.get(self.url)

        response = self.mapbased_view.list(request)


class GigaPixelStoryMapWidgetTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.gigapixel_view = BaseStoryMapGPView()

        self.url = reverse('examplestorymapgp-list')

    def get_storymap_options(self):
        return {
            "map_type": "zoomify",
            "map_background_color": "#333",
            "map_as_image": True,
            "calculate_zoom": False,
            "zoomify": {
                "path": "http://cdn.verite.co/maps/zoomify/seurat/",
                "width": 30000,
                "height": 19970,
                "tolerance": 0.9,
                "attribution": "<a href='http://www.google.com/culturalinstitute/asset-viewer/a-sunday-on-la-grande-jatte-1884/twGyqq52R-lYpA?projectId=art-project' target='_blank'>Google Art Project</a>"
            }
        }

    def test_assert_response_valid_data(self):
        request = self.factory.get(self.url)
        response = self.gigapixel_view.list(request)

        self.assertEqual(response.status_code, 200)

    def test_assert_response_invalid_data(self):
        request = self.factory.get(self.url)

        def get_font():
            return 'stock:opensans-gentiumbook'

        def get_storymap_body():
            return {
                "map_type": "zoomify",
                "slides": [
                    {
                        "date": "",
                        "location": {
                            "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                            "line": True
                        },
                        "background": {
                            "url": "http://gigapixel.knightlab.com/seurat/seurat_portrait.jpg",
                            "color": "#000",
                            "opacity": 50
                        },
                        "text": {
                            "headline": "A Sunday on La Grande Jatte <br><small>Georges Seurat</small>",
                            "text": "In his best-known and largest painting, Georges Seurat depicted people relaxing in a suburban park on an island in the Seine River called La Grande Jatte."
                        },
                        "type": "overview"
                    },
                    {
                        "date": "",
                        "location": {
                            "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                            "lat": 75.71563324165896,
                            "line": True,
                            "lon": -132.1875,
                            "zoom": 6
                        },
                        "text": {
                            "headline": "Small Horizontal Brushstrokes",
                            "text": "Work began in 1884. The artist worked on the painting in several campaigns, beginning in 1884 with a layer of small horizontal brushstrokes of complementary colors."
                        }
                    }
                ],
                "zoomify": {
                    "attribution": "",
                    "height": 19970,
                    "path": "http://gigapixel.knightlab.com/seurat/",
                    "tolerance": 0.9,
                    "width": 30000
                }
            }

        self.gigapixel_view.get_font_css = get_font
        self.gigapixel_view.get_storymap = get_storymap_body

        response = self.gigapixel_view.list('')
        self.assertEqual(response.status_code, 200)

