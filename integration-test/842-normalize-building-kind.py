# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class NormalizeBuildingKind(FixtureTest):
    def test_office(self):
        self.generate_fixtures(dsl.way(431358377, wkt_loads('POLYGON ((127.055528903431 37.25885030044089, 127.056004112216 37.2594416554027, 127.05683658099 37.2590179623059, 127.056361372205 37.25842660401769, 127.055528903431 37.25885030044089))'), {u'building': u'office', u'building:levels': u'25', u'way_area': u'10799.6', u'name': u'R5 Tower A', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 55897, 25449, 'buildings',
            {'id': 431358377, 'kind': 'building', 'kind_detail': 'office'})

    def test_apartments(self):
        self.generate_fixtures(dsl.way(264768910, wkt_loads('POLYGON ((-73.98828849563579 40.74023561233388, -73.98813551254288 40.7404461995804, -73.9881196123624 40.74046341951649, -73.98828229726038 40.74053127827239, -73.9882283983433 40.74060587518007, -73.9881381176572 40.740730021673, -73.9881126055032 40.7407646655817, -73.9878740129637 40.74066440919139, -73.9880434352263 40.74043129378239, -73.988048825118 40.74042271784228, -73.9880213366703 40.7404112151907, -73.98817584689918 40.7401985859359, -73.988181596117 40.74019055447189, -73.98828849563579 40.74023561233388))'), {u'building': u'apartments', u'building:colour': u'#92A39B', u'alt_name': u'One Madison Park', u'name': u'One Madison', u'roof:shape': u'flat', u'building:material': u'glass', u'addr:postcode': u'10010', u'roof:material': u'concrete', u'way_area': u'1705.96', u'wikipedia': u'en:One Madison', u'height': u'22.1', u'building:part': u'yes', u'addr:street': u'East 22nd Street', u'wikidata': u'Q7092848', u'source': u'openstreetmap.org', u'addr:housenumber': u'23', u'nycdoitt:bin': u'1087769', u'start_date': u'2010', u'addr:city': u'New York'}))  # noqa

        self.assert_has_feature(
            16, 19298, 24633, 'buildings',
            {'id': 264768910, 'kind': 'building', 'kind_detail': 'apartments'})

    def test_transportation(self):
        # Way: Forest Hill (136822046)
        self.generate_fixtures(dsl.way(136822046, wkt_loads('POLYGON ((-122.459306298082 37.74808385365419, -122.45921098683 37.7481533926691, -122.459174335567 37.74812249434061, -122.4591610405 37.74813187038649, -122.459014345615 37.74800600397469, -122.459041295073 37.74798625741889, -122.459020005001 37.74796800250468, -122.459031862763 37.74795940777698, -122.459021801631 37.74795116820238, -122.459007069261 37.7479618228245, -122.458918764868 37.74788617497398, -122.458982275759 37.7478397917936, -122.458992965711 37.74784888375169, -122.459046774796 37.74780960364378, -122.459112711138 37.74786607323168, -122.459059620705 37.74790485609358, -122.459071298804 37.74791487144469, -122.459050817215 37.74792978792259, -122.459060788515 37.7479381695613, -122.459085492185 37.74792026978948, -122.459106872089 37.74793859574629, -122.459134270705 37.74791849401819, -122.459282043569 37.74804521294759, -122.459270545134 37.74805359457319, -122.459306298082 37.74808385365419))'), {u'building': u'station', u'addr:housenumber': u'380', u'name': u'Forest Hill', u'source': u'openstreetmap.org', u'addr:postcode': u'94116', u'way_area': u'794.648', u'wikipedia': u'en:Forest Hill Station (San Francisco)', u'addr:state': u'CA', u'platforms': u'2', u'wikidata': u'Q5468939', u'subway': u'yes', u'old_name': u'Laguna Honda', u'operator': u'San Francisco Municipal Railway', u'railway': u'station', u'addr:street': u'Laguna Honda Boulevard', u'addr:country': u'US', u'addr:city': u'San Francisco'}))  # noqa

        self.assert_has_feature(
            16, 10474, 25337, 'buildings',
            {'id': 136822046, 'kind': 'building',
             'kind_detail': 'transportation'})

    def test_building_no_detail(self):
        self.generate_fixtures(dsl.way(93817368, wkt_loads('POLYGON ((-122.391617882097 37.79075260841837, -122.39157161886 37.79078881316559, -122.391613121026 37.79082196534019, -122.391354316393 37.79102400161111, -122.391328175418 37.79100305971841, -122.39120896898 37.79109605587491, -122.391238882879 37.79111997929478, -122.390975407006 37.79132570618769, -122.390349191422 37.7908246629468, -122.390613296115 37.79061857970968, -122.390641503215 37.7906411544774, -122.390754331615 37.79055319803199, -122.390713098943 37.79052025870667, -122.390989690219 37.79030451996099, -122.391029395755 37.79033618156039, -122.39106380123 37.7903092763008, -122.391617882097 37.79075260841837))'), {u'building': u'yes', u'addr:housenumber': u'2', u'way_area': u'10496.7', u'height': u'91 m', u'source': u'openstreetmap.org', u'addr:street': u'Folsom Street'}))  # noqa

        self.assert_has_feature(
            16, 10487, 25327, 'buildings',
            {'id': 93817368, 'kind': 'building', 'kind_detail': type(None)})

    def test_building_part_no_detail(self):
        self.generate_fixtures(dsl.way(132605515, wkt_loads('POLYGON ((-122.419354803799 37.77140395803509, -122.419149538757 37.77183071670441, -122.419103994172 37.7718149529505, -122.419095280513 37.77183511919369, -122.418998531957 37.77180557990599, -122.419007604942 37.77178548466268, -122.41895047209 37.77176858477179, -122.41895460434 37.77175928272939, -122.418908880092 37.77174635927928, -122.418703165892 37.7717401105773, -122.418631839658 37.77176169700008, -122.418608393629 37.7717717091217, -122.418612795374 37.77178711784519, -122.418509219622 37.77180337866049, -122.41846205807 37.77179691693959, -122.418301978286 37.77128430894781, -122.418536977564 37.77130000180649, -122.418550092968 37.771346370279, -122.41858548659 37.771339695493, -122.418656902655 37.77157402272518, -122.418669838395 37.77157402272518, -122.418684660597 37.77157402272518, -122.418684301271 37.77155889798988, -122.418961611199 37.7715704723181, -122.418957389117 37.77162635570561, -122.419009401572 37.77162948006139, -122.419025571247 37.77160746755138, -122.419025211921 37.771587798303, -122.418992333582 37.77157700506699, -122.419067073414 37.77143300042538, -122.419090609274 37.771439178145, -122.419106599286 37.7714001235867, -122.419117199406 37.7714022538359, -122.419123218119 37.77138911729829, -122.419128158853 37.77137796899169, -122.419354803799 37.77140395803509))'), {u'building:part': u'apartments', u'building:levels': u'11', u'way_area': u'4455.76', u'source': u'openstreetmap.org', u'height': u'50 m'}))  # noqa

        self.assert_has_feature(
            16, 10482, 25331, 'buildings',
            {'id': 132605515, 'kind': 'building_part',
             'kind_detail': type(None)})

        self.generate_fixtures(dsl.way(406710839, wkt_loads('POLYGON ((-122.393609087756 37.79544282119438, -122.393608997925 37.7954436020317, -122.393608458935 37.79544445385419, -122.393607740283 37.79544509272108, -122.393606662305 37.7954455896176, -122.393605584327 37.79544566060279, -122.393604506348 37.7954455896176, -122.393603518201 37.79544509272108, -122.393602799549 37.79544445385419, -122.39360226056 37.79544367301688, -122.393602170728 37.79544282119438, -122.393602530055 37.7954418983866, -122.393603069044 37.7954411885345, -122.393603967359 37.7954406206528, -122.393605045337 37.79544026572668, -122.393606213147 37.79544026572668, -122.393607201294 37.7954406206528, -122.393608099609 37.7954411175493, -122.393608818262 37.7954418983866, -122.393609087756 37.79544282119438))'), {u'building:part': u'yes', u'source': u'openstreetmap.org', u'way_area': u'0.4508', u'height': u'83.1 m'}))  # noqa

        self.assert_has_feature(
            16, 10486, 25326, 'buildings',
            {'id': 406710839, 'kind': 'building_part',
             'kind_detail': type(None)})

    def test_steps(self):
        self.generate_fixtures(dsl.way(257920199, wkt_loads('POLYGON ((-77.0366387672893 38.8977957751656, -77.03663867745769 38.89782527842089, -77.03645910423239 38.897825208508, -77.03645928389548 38.89779521586208, -77.0364637754719 38.89779521586208, -77.03656851903401 38.89779535568799, -77.03663140110389 38.8977955654268, -77.0366387672893 38.8977957751656))'), {u'roof:slope:direction': u'0', u'building:colour': u'lightgray', u'way_area': u'85.4211', u'source': u'openstreetmap.org', u'building:part': u'steps', u'roof:colour': u'lightgray', u'roof:height': u'1.5', u'height': u'1.5', u'roof:shape': u'skillion'}))  # noqa

        self.assert_has_feature(
            16, 18743, 25070, 'buildings',
            {'id': 257920199, 'kind': 'building_part', 'kind_detail': 'steps'})

        self.generate_fixtures(dsl.way(352508405, wkt_loads('POLYGON ((-16.8258220249888 28.20356598707959, -16.8257906737854 28.20359385357621, -16.8257773787192 28.20358031615968, -16.8258089994172 28.2035533204878, -16.8258220249888 28.20356598707959))'), {u'building:part': u'stairs', u'building:levels': u'4', u'way_area': u'10.877', u'source': u'openstreetmap.org', u'height': u'12'}))  # noqa

        self.assert_has_feature(
            16, 29704, 27412, 'buildings',
            {'id': 352508405, 'kind': 'building_part', 'kind_detail': 'steps'})
