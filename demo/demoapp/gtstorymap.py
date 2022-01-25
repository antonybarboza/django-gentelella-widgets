from djgentelella.groute import register_lookups
from djgentelella.views.storymap import BaseStoryMapGPView, BaseStoryMapMBView


@register_lookups(prefix="gigapixel_storymap", basename="examplestorymapgp")
class GigaPixelStoryMapExample(BaseStoryMapGPView):

    def get_font_css(self):
        return 'stock:opensans-gentiumbook'

    def get_storymap(self):
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
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": 77.62241984285832,
                        "line": True,
                        "lon": -20.478515625,
                        "zoom": 4
                    },
                    "media": {
                        "caption": "",
                        "credit": "",
                        "url": ""
                    },
                    "text": {
                        "headline": "Complementary Colors",
                        "text": "The complementary colors give the painting a unified sense of color"
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": 77.62241984285832,
                        "line": True,
                        "lon": -20.478515625,
                        "zoom": 7
                    },
                    "media": {
                        "caption": "",
                        "credit": "",
                        "url": ""
                    },
                    "text": {
                        "headline": "Small Dots",
                        "text": "He later added small dots, also in complementary colors."
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": 77.62241984285832,
                        "line": True,
                        "lon": -20.478515625,
                        "zoom": 4
                    },
                    "media": {
                        "caption": "Seurat made several studies for the large painting including a smaller version. Study for La Grand Jatte, 1884. ",
                        "credit": "Georges Seurat",
                        "url": "http://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Study_for_La_Grande_Jatte%2C_Georges_Seurat%2C_1884.jpg/800px-Study_for_La_Grande_Jatte%2C_Georges_Seurat%2C_1884.jpg"
                    },
                    "text": {
                        "headline": "Dots as Solid Forms from a Distance",
                        "text": "The dots appear as solid and luminous forms when seen from a distance."
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": 77.63654163009744,
                        "line": True,
                        "lon": 79.62890625,
                        "zoom": 7
                    },
                    "media": {
                        "caption": "",
                        "credit": "",
                        "url": "http://en.wikipedia.org/wiki/Pointillism"
                    },
                    "text": {
                        "headline": "Pointillism",
                        "text": "Seurat's use of this highly systematic and \"scientific\" technique, subsequently called Pointillism, distinguished his art from the more intuitive approach to painting used by the Impressionists."
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": 72.71190310803662,
                        "line": True,
                        "lon": -9.140625,
                        "zoom": 4
                    },
                    "media": {
                        "caption": "La plage de Trouville, 1870, National Gallery, London. ",
                        "credit": "Claude Monet",
                        "url": "http://upload.wikimedia.org/wikipedia/commons/d/df/Claude_Monet_002.jpg"
                    },
                    "text": {
                        "headline": "Modern Life",
                        "text": "Although Seurat embraced the subject matter of modern life preferred by artists such as Claude Monet and Pierre-Auguste Renoir, he went beyond their concern for capturing the accidental and instantaneous qualities of light in nature."
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": 75.32002523220804,
                        "line": True,
                        "lon": 49.5703125,
                        "zoom": 5
                    },
                    "media": {
                        "caption": "Riace bronzes, examples of proto classic bronze sculpture",
                        "credit": "<a href='http://en.wikipedia.org/wiki/Ancient_Greek_sculpture' target='_blank'>Wikipedia</a>",
                        "url": "http://upload.wikimedia.org/wikipedia/commons/9/96/Reggio_calabria_museo_nazionale_bronzi_di_riace.jpg"
                    },
                    "text": {
                        "headline": "Permanence",
                        "text": "Seurat sought to evoke permanence by recalling the art of the past, especially Egyptian and Greek sculpture and even Italian Renaissance frescoes."
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": 75.45307133006602,
                        "line": True,
                        "lon": -65.126953125,
                        "zoom": 4
                    },
                    "media": {
                        "caption": "Cattle led to sacrifice, South XLV, 137–140, British Museum.",
                        "credit": "Wikipedia",
                        "url": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Sacrifice_south_frieze_Parthenon_BM.jpg/794px-Sacrifice_south_frieze_Parthenon_BM.jpg"
                    },
                    "text": {
                        "headline": "Procession",
                        "text": "Seurat explained to the French poet Gustave Kahn, \"The Panathenaeans of Phidias formed a procession. I want to make modern people, in their essential traits, move about as they do on those friezes, and place them on canvases organized by harmonies of color.\""
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": 17.14079039331665,
                        "line": True,
                        "lon": -95.44921875,
                        "zoom": 4
                    },
                    "media": {
                        "caption": "",
                        "credit": "",
                        "url": "<blockquote><p>faux Puvis de Chavannes</p><cite>Art Critic Paul Alexis</cite></blockquote>"
                    },
                    "text": {
                        "headline": "Critics",
                        "text": "Some contemporary critics, however, found his figures to be less a nod to earlier art history than a commentary on the posturing and artificiality of modern Parisian society."
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": -35.46066995149529,
                        "line": True,
                        "lon": -99.84374999999999,
                        "zoom": 6
                    },
                    "media": {
                        "caption": "",
                        "credit": "",
                        "url": ""
                    },
                    "text": {
                        "headline": "Frame",
                        "text": "Seurat made the final changes to La Grande Jatte in 1889. He restretched the canvas in order to add a painted border of red, orange, and blue dots that provides a visual transition between the interior of the painting and his specially designed white frame."
                    }
                },
                {
                    "date": "",
                    "location": {
                        "icon": "http://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/blue-pushpin.png",
                        "lat": -30.826780904779774,
                        "line": True,
                        "lon": 128.056640625,
                        "zoom": 5
                    },
                    "media": {
                        "caption": "",
                        "credit": "",
                        "url": "http://en.wikipedia.org/wiki/Georges_Seurat"
                    },
                    "text": {
                        "headline": "Inscriptions",
                        "text": "Inscribed at lower right: Seurat"
                    }
                },
                {
                    "date": "",
                    "media": {
                        "caption": "Island of La Grande Jatte",
                        "credit": "Stamen Maps",
                        "url": "https://s3.amazonaws.com/images.m2i.stamen.com/20140221/toner_uC3-XT7eNGQ.png"
                    },
                    "text": {
                        "headline": "Info",
                        "text": "a"
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


@register_lookups(prefix="mapbased_storymap", basename="examplestorymapmb")
class MapBasedStoryMapExample(BaseStoryMapMBView):
    def get_storymap(self):
        return {
            "slides": [{
                "type": "overview",
                "date": "1790-2010",
                "text": {
                    "headline": "US Westward Expansion <small>Mean center of United States population</small>",
                    "text": "<p>The mean center of U.S. population is determined by the United States Census Bureau from the results of each census. Defined as the point at which an imaginary, flat, weightless, and rigid map of the United States would balance perfectly if weights of identical value were placed on it so that each weight represented the location of one person on the date of the census.</p> <span class='vco-note'>This is an overview or title slide to show all the points in your story routed on your map.</span>"
                },
                "media": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/US_Mean_Center_of_Population_1790-2010.PNG/800px-US_Mean_Center_of_Population_1790-2010.PNG",
                    "credit": "wikipedia",
                    "caption": "Mean US_Mean_Center_of_Population_1790-2010"
                }
            }, {
                "date": "1790",
                "text": {
                    "headline": "1790",
                    "text": "<p>A look at the US during this first Census data collection.</p> <span class='vco-note'>Map (left) is an example of a URL to an image hosted on the web.</span>"
                },
                "location": {
                    "name": "Kent County, Maryland",
                    "lat": 39.27500,
                    "lon": -76.18667,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/2/2e/United_States_1789-08-1790.png",
                    "credit": "photobucket",
                    "caption": "1790 Map of the US Census"
                }
            }, {
                "date": "1800",
                "text": {
                    "headline": "1800: Thomas Jefferson",
                    "text": "<p>In 1800, Thomas Jefferson was elected as the President of the United States, not too far from Howard County Maryland the new center of US population. He of course did not have a Twitter account, but this is fun.</p> <span class='vco-note'>You can embed a tweet into your StoryMapJS using the URL to the tweet.</span>"
                },
                "location": {
                    "name": "Howard County, Maryland",
                    "lat": 39.26833,
                    "lon": -76.94167,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://twitter.com/ThomasJefferson/status/265523460720168960",
                    "credit": "Twitter",
                    "caption": "Thomas Jefferson Twitter account"
                }
            }, {
                "date": "1810",
                "text": {
                    "headline": "1810: Loudoun County, Virginia",
                    "text": "<p>The population moved 40 miles northwest of Washington, DC. The US also acquired new territory west of the original 13 states in 1803 through the Louisiana Purchase from France.</p> <span class='vco-note'>The headline and location name to the previous and next slide (left and right), show up under the navigation arrows.</span>"
                },
                "location": {
                    "name": "Loudoun County, Virginia",
                    "lat": 39.19167,
                    "lon": -77.62000,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "http://www.worldmapsonline.com/images/Cram/History/unitedstates1810.jpg",
                    "credit": "worldmapsonline",
                    "caption": "1810 Map of the US"
                }
            }, {
                "date": "1820",
                "text": {
                    "headline": "1820: Census image from Flickr",
                    "text": "<p>The mean population has moved into what is now West Virginia.</p> <span class='vco-note'>This example of an 1820 Census record pulled from Flickr gives an example of how the Census was conducted by hand.</span>"
                },
                "location": {
                    "name": "Hardy County, Virginia (now W. Virginia)",
                    "lat": 39.09500,
                    "lon": -78.55000,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "http://www.flickr.com/photos/graysonfamily/349095341/",
                    "credit": "graysonfamily",
                    "caption": "1820 Census Record"
                }
            }, {
                "date": "1830",
                "text": {
                    "headline": "1830: Old state lines of Virginia",
                    "text": "A cool map showing how West Virginia was once part of Virginia. It is the only state to form by seceding from a Confederate state, it did so in 1863 and was almost named the State of Kanawha."
                },
                "location": {
                    "name": "Grant County, Virginia (now W. Virginia)",
                    "lat": 38.96500,
                    "lon": -79.28167,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "http://www.virginiaplaces.org/boundaries/graphics/kanawha1862.png",
                    "credit": "Virginia Places",
                    "caption": "Map of Virginia"
                }
            }, {
                "date": "1840",
                "text": {
                    "headline": "1840: Annexation of Texas",
                    "text": "<p>The mean population has moved into Upshur County, Virginia (now W. Virginia). By the mid 1840s the US was fighting the Mexican American War with one of the results being the annexation of Texas.</p> <span class='vco-note'>You can add a YouTube URL like this Crash Course on the Mexican American War.</span>"
                },
                "location": {
                    "name": "Upshur County, Virginia (now W. Virginia)",
                    "lat": 39.03333,
                    "lon": -80.30000,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://www.youtube.com/watch?v=tkdF8pOFUfI",
                    "credit": "crashcourse",
                    "caption": "Crash Course on the Mexican American War"
                }
            }, {
                "date": "1850",
                "text": {
                    "headline": "1850: Uncle Tom's Cabin",
                    "text": "<p>The mean is in Wirt County in what is now West Virginia. In 1852, Harriet Beecher Stowe's 'Uncle Tom's Cabin' was published, galvanizing the abolitionist movement.</p> <span class='vco-note'>Embed a YouTube URL like this one about Uncle Tom's Cabin.</span>"
                },
                "location": {
                    "name": "Wirt County, Virginia (now W. Virginia)",
                    "lat": 38.98333,
                    "lon": -81.31667,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://www.youtube.com/watch?v=CZCsBCio41k",
                    "credit": "Appucator",
                    "caption": "Uncle Tom's Cabin (1903 Silent Film)"
                }
            }, {
                "date": "1860",
                "text": {
                    "headline": "1860: Abraham Lincoln",
                    "text": "<p>Abraham Lincoln is elected as the 16th President of the U.S.</p> <span class='vco-note'>This excerpt is embedded from Wikipedia</span></p>."
                },
                "location": {
                    "name": "Pike County, Ohio",
                    "lat": 39.00667,
                    "lon": -82.81333,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://en.wikipedia.org/wiki/Abraham_Lincoln",
                    "credit": "wikipedia",
                    "caption": "1860 Abraham Lincoln elected President"
                }
            }, {
                "date": "1870",
                "text": {
                    "headline": "1870: Finally counting everyone",
                    "text": "This census was the first to record the names and other personal information of all African-Americans, including those who were formerly enslaved. In researching your African-American ancestors, moving backward from the present, the 1870 federal census may be the last census in which you are able to identify these ancestors by name. The 1870 census often even serves as a powerful tool in identifying former slave owners, a necessary step for anyone desiring to reclaim the heritage of their enslaved ancestors."
                },
                "location": {
                    "name": "Highland County, Ohio",
                    "lat": 39.20000,
                    "lon": -83.59500,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://www.archives.gov/exhibits/treasures_of_congress/Images/page_13/47a.jpg",
                    "credit": "Archives.gov",
                    "caption": "41st & 42nd Congress newly elected"
                }
            }, {
                "date": "1880",
                "text": {
                    "headline": "1880: Decade when film is created",
                    "text": "<p>The mean is in Boone County, Kentucky, 8 miles west by south of Cincinnati, OH. Here are some frames from film pioneer Louis Le Prince's record of Leeds Bridge and horse traffic made as a series of glass plates in 1889 (some sources say paper). The first film ever made.</p> <span class='vco-note'>Embed videos from YouTube.</span>"
                },
                "location": {
                    "name": "Boone County, Kentucky",
                    "lat": 39.06889,
                    "lon": -84.66111,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://www.youtube.com/watch?v=C-nTpGMMVjY",
                    "credit": "Huntley Film Archives",
                    "caption": "Frames Louis Le Prince's record of Leeds Bridge"
                }
            }, {
                "date": "1890",
                "text": {
                    "headline": "1890: Columbus, IN Plane Crash",
                    "text": "<p>Mean population is now 20 miles east of Columbus, IN. On July 25, 2013, a plane crashed into a house in Columbus.</p> <span class='vco-note'>Using a Storify URL you can embed the sequence of events.</span>"
                },
                "location": {
                    "name": "Decatur County, Indiana",
                    "lat": 39.19889,
                    "lon": -85.54806,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://storify.com/EJSham/minute-by-minute-coverage-of-the-columbus-indiana",
                    "credit": "Ebony Shamberger",
                    "caption": "Minute-by-minute coverage of the Columbus, Indiana, plane crash"
                }
            }, {
                "date": "1900",
                "text": {
                    "headline": "1900: Hear some music from the time",
                    "text": "<p>The mean population is now 6 miles southeast of Columbus. Listen to 'In the sweet bye and bye' by Harry MacDonough. Original recording by Roger Harding released in 1898. Popular music from 1900-1910.</p> <span class='vco-note'>Embed soundclips from Soundcloud.</span>"
                },
                "location": {
                    "name": "Bartholomew County, Indiana",
                    "lat": 39.16000,
                    "lon": -85.81500,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://soundcloud.com/mister-click/harry-macdonough-in-the-sweet",
                    "credit": "Soundcloud",
                    "caption": "In the sweet bye and bye"
                }
            }, {
                "date": "1910",
                "text": {
                    "headline": "1910: Old Photos",
                    "text": "The mean is now in the city of Bloomington. Which had the University of Indiana since 1820. In 1910 the population was 8,838 people. One hundred years later in 2010 the population was 80,405 people."
                },
                "location": {
                    "name": "Monroe County, Indiana",
                    "lat": 39.17000,
                    "lon": -86.53889,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/US-center-pop.jpg/471px-US-center-pop.jpg",
                    "credit": "wikipedia",
                    "caption": "1910 Center of the US Population"
                }
            }, {
                "date": "1920",
                "text": {
                    "headline": "1920: An American in the Making",
                    "text": "<p>An old film from the time showing Gary, Indiana, which is near Owen County where the population mean is in 1920. Director/Photographer: Carl Lewis Gregory, Locations: Ellis Island in New York Harbor; the Gary, Indiana works of the United States Steel Corporation.</p> <span class='vco-note'>Embed a Vimeo.</span>"
                },
                "location": {
                    "name": "Owen County, Indiana",
                    "lat": 39.17250,
                    "lon": -86.72083,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://vimeo.com/63929704",
                    "credit": "Ned Thanhouser",
                    "caption": "An American in the Making"
                }
            }, {
                "date": "1930",
                "text": {
                    "headline": "1930: Dorothy as a kid",
                    "text": "<p>Greene County, Indiana located 3 miles northeast of Linton. Judy Garland singing 'Bubbles' from 1930.</p> <span class='vco-note'>Embed from Daily Motion.</span>"
                },
                "location": {
                    "name": "Greene County, Indiana",
                    "lat": 39.06250,
                    "lon": -87.13500,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://www.youtube.com/watch?v=xp9kONt2X54",
                    "credit": "You Tube",
                    "caption": "Judy Garland 1930"
                }
            }, {
                "date": "1940",
                "text": {
                    "headline": "1940: World at war",
                    "text": "The mean population has moved to Sullivan County, Indiana, 2 miles southeast by east of Carlisle. Here is a newspaper from 1941, Chicago Tribune publisher Col. Robert McCormick had been opposed to the U.S. getting into a war with Japan, but once war was declared, the Tribune lines up solidly behind FDR's war efforts."
                },
                "location": {
                    "name": "Sullivan County, Indiana",
                    "lat": 38.94833,
                    "lon": -87.37639,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://illinoisstatesoceity.typepad.com/photos/19411950_illinois_state_s/pearl5.jpg",
                    "credit": "Illinois State Society",
                    "caption": "Chicago Tribune front page 1941"
                }
            }, {
                "date": "1950",
                "text": {
                    "headline": "1950: Video about the railroads",
                    "text": "Richland County, Illinois is the new mean center of the US. Here is an educational documentary from the time by the 31 members of the Illinois Association of Railroads. It examines the problems facing railroads in the 1950's such as competition from cars, trucks and planes, as well as the unfair tax burden faced by railroads at the time."
                },
                "location": {
                    "name": "Richland County, Illinois",
                    "lat": 38.83917,
                    "lon": -88.15917,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://www.youtube.com/watch?v=ElyERLwsV0c",
                    "credit": "WDTVLIVE42",
                    "caption": "Illinois RailRoads 1950s"
                }
            }, {
                "date": "1960",
                "text": {
                    "headline": "1960: Chicago Blues",
                    "text": "<p>Clinton County, Illinois has become the new mean of the populatin as it moves west. This is the time period of Chicago Blues and Chess Records released the Best of Muddy Waters which included this song.</p> <span class='vco-note'>Embed a Soundcloud track</span>"
                },
                "location": {
                    "name": "Clinton County, Illinois",
                    "lat": 38.59944,
                    "lon": -89.20972,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://soundcloud.com/carolebphotographe/4-muddy-waters-louisiana-blues",
                    "credit": "Soundcloud",
                    "caption": "Muddy Waters - Louisiana Blues"
                }
            }, {
                "date": "1970",
                "text": {
                    "headline": "1970: To the Moon!",
                    "text": "St. Clair County, Illinois is the new population center. In 1969, the US not only went west, but landed on the moon! Check out this cool <b>Vimeo</b> of the Apollo 11 trip in 100 seconds."
                },
                "location": {
                    "name": "St. Clair County, Illinois",
                    "lat": 38.46306,
                    "lon": -89.70611,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://vimeo.com/62707231",
                    "credit": "Spacecraft Films",
                    "caption": "Apollo 11 in 100 seconds"
                }
            }, {
                "date": "1980",
                "text": {
                    "headline": "1980: Westward ho!",
                    "text": "Jefferson County, Missouri a 1/4 mile west of DeSoto. This is the first year that the mean was outside and west of the territory of the original 13 states."
                },
                "location": {
                    "name": "Jefferson County, Missouri",
                    "lat": 38.13694,
                    "lon": -90.57389,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Territorial-acquisition-uscensus-bureau.jpg",
                    "credit": "wikimedia",
                    "caption": "United States Territories"
                }
            }, {
                "date": "1990",
                "text": {
                    "headline": "1990: Hubble",
                    "text": "<p>The US mean moved west to Crawford County, Missouri, but the US again makes a leap into space, launching the Hubble telescope.</p> <span class='vco-note'>YouTube video featuring images taken by Hubble space telescope.</span>"
                },
                "location": {
                    "name": "Crawford County, Missouri",
                    "lat": 37.87222,
                    "lon": -91.21528,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://www.youtube.com/watch?v=z_ISPDTpJrk",
                    "credit": "Coconut Science Lab",
                    "caption": "Best of Hubble"
                }
            }, {
                "date": "2000",
                "text": {
                    "headline": "2000: A new millenium",
                    "text": "<p>Phelps County, Missouri is the new center of US population. Here's a good laugh and some good perspective, remember Y2K?</p> <span class='vco-note'>YouTube video</span>"
                },
                "location": {
                    "name": "Phelps County, Missouri",
                    "lat": 37.696987,
                    "lon": -91.809567,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://www.youtube.com/watch?v=X_KoNZkf-2k",
                    "credit": "KGBT",
                    "caption": "Valley Residents Prepare for Y2K"
                }
            }, {
                "date": "2010",
                "text": {
                    "headline": "2010: And Twitter happened",
                    "text": "<p>The new center is Texas County, Missouri, which has nothing to do with Texas. In the past decade many things happened but a big one is the founding of Twitter in 2006. Here is the #1 most retweeted tweet from 2010.</p> <span class='vco-note'>Another example of an embedded tweet.</span>"
                },
                "location": {
                    "name": "Texas County, Missouri",
                    "lat": 37.517534,
                    "lon": -92.173096,
                    "zoom": 10,
                    "line": True
                },
                "media": {
                    "url": "https://twitter.com/StephenAtHome/status/16360461594",
                    "credit": "Twitter",
                    "caption": "Stephen Colbert"
                }
            }]
        }
