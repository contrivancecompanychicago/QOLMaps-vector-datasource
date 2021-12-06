# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class BicycleYesDesignatedRoads(FixtureTest):

    def test_bicycle_yes(self):
        # Add bicycle properties to roads
        # Road with bicycle=yes in Washington, DC
        self.generate_fixtures(dsl.way(49724285, wkt_loads('POINT (-76.9522159053715 38.86525601448588)'), {u'source': u'openstreetmap.org', u'traffic_signals': u'signal', u'highway': u'traffic_signals'}), dsl.way(281677984, wkt_loads('LINESTRING (-76.958525312601 38.86199860279859, -76.9576779317935 38.86219697553369, -76.95749090255129 38.86224300128667, -76.95731303612509 38.86231141032949, -76.9571003150658 38.86241199528519, -76.95697383227379 38.86249502323249, -76.95683890531809 38.8625953980857, -76.95670128341661 38.86272228288901, -76.95659788732739 38.86285798082939, -76.95631491801289 38.86324199060768, -76.9560639287225 38.86358997581961, -76.95603293684522 38.86362900601449, -76.95601586885481 38.86364698227989, -76.9559998788428 38.86366600773868, -76.95596493437819 38.86370196024618, -76.9559458900942 38.86371895724239, -76.9558938776392 38.86377001815309, -76.9558589331747 38.8638029629131, -76.955821922585 38.86383597760408, -76.95578491199528 38.86386696383619, -76.95574592511188 38.86389802000109, -76.95563992390839 38.8639730023973, -76.95548487469038 38.8640659608739, -76.9554318740886 38.86409498851478, -76.95532389659149 38.86414800764509, -76.95521286482229 38.86419696986749, -76.95498190796279 38.8642819542163, -76.95373594466369 38.86471995424531, -76.95294093563729 38.86499896627109, -76.9522159053715 38.86525601448588, -76.95170557245859 38.86543759138589)'), {
                               u'source:HFCS': u'District of Columbia (DC GIS)', u'tiger:name_base': u'Alabama', u'lanes': u'4', u'name': u'Alabama Avenue Southeast', u'tiger:cfcc': u'A41', u'tiger:zip_left': u'20020', u'tiger:name_direction_suffix': u'SE', u'tiger:zip_right': u'20020', u'source': u'openstreetmap.org', u'tiger:county': u'District of Columbia, DC', u'tiger:name_type': u'Ave', u'bicycle': u'yes', u'HFCS': u'Minor Arterial', u'highway': u'secondary'}))

        self.assert_has_feature(
            16, 18758, 25078, 'roads',
            {'id': 281677984, 'kind': 'major_road',
             'is_bicycle_related': True, 'bicycle': 'yes'})

    def test_bicycle_designated(self):
        # Road with bicycle=designated in Eureka, California
        self.generate_fixtures(dsl.way(1476087037, wkt_loads('POINT (-124.172141567461 40.80012426290038)'), {u'source': u'openstreetmap.org', u'highway': u'stop'}), dsl.way(1491131038, wkt_loads('POINT (-124.171947800854 40.7993163954652)'), {u'source': u'openstreetmap.org', u'highway': u'stop'}), dsl.way(1491131050, wkt_loads('POINT (-124.171985979253 40.7994806218385)'), {u'source': u'openstreetmap.org', u'highway': u'stop'}), dsl.way(10273013, wkt_loads(
            'LINESTRING (-124.171938907533 40.78046798963329, -124.171923905667 40.78167428133911, -124.171924893814 40.7821939581685, -124.171913934368 40.78290197729467, -124.171904861383 40.78412999064899, -124.171904861383 40.78428296358129, -124.171904591889 40.7843641091512, -124.171903873236 40.78451599325818, -124.171897944356 40.7853639667952, -124.171881864512 40.78619206878748, -124.171873959338 40.78698941752269, -124.171877911925 40.78782035585549, -124.1718658745 40.7888099594419, -124.171854915054 40.7889719673665, -124.171838925041 40.78980050045539, -124.171834792791 40.79063745664679, -124.171834792791 40.79103960810009, -124.171838925041 40.79146800927739, -124.171834972454 40.79214818143286, -124.171836858916 40.79232997209088, -124.171834882623 40.79282997884548, -124.17182589947 40.7934670195374, -124.171821857051 40.7940889563253, -124.171864796522 40.794491018866, -124.17186353888 40.79491001277599, -124.171867401636 40.79532798393959, -124.171854196401 40.79573840376309, -124.171853837075 40.79615052119841, -124.171846830216 40.79656488025841, -124.171839643694 40.7969661797482, -124.17183533178 40.79738345791941, -124.171827965595 40.79779447707399, -124.171832996161 40.79821277009649, -124.17182589947 40.79867641875239, -124.171824462165 40.7987470742253, -124.171829402899 40.7988084811826, -124.171840991167 40.79886227172638, -124.171856891347 40.79892265853029, -124.171904771552 40.79913305987029, -124.171947800854 40.7993163954652, -124.171964689181 40.79939269447679, -124.171985979253 40.7994806218385, -124.172141567461 40.80012426290038, -124.172156030337 40.80019756890339)'), {u'tiger:name_base': u'California', u'bicycle': u'designated', u'name': u'California Street', u'tiger:cfcc': u'A41', u'tiger:reviewed': u'yes', u'source': u'openstreetmap.org', u'tiger:county': u'Humboldt, CA', u'tiger:name_type': u'St', u'highway': u'tertiary'}))

        self.assert_has_feature(
            16, 10163, 24621, 'roads',
            {'id': 10273013, 'kind': 'major_road',
             'is_bicycle_related': True, 'bicycle': 'designated'})
