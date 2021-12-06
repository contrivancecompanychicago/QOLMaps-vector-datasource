# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class CategorizeTrains(FixtureTest):
    def test_long_distance(self):
        import dsl

        z, x, y = 5, 5, 11
        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/2812900
            dsl.way(2812900, dsl.tile_diagonal(z, x, y), {
                "FIXME": "Underlying infrastructure \"Seattle Subdivision\"" \
                "needs some fixing",
                "colour": "#191970",
                "from": "Los Angeles",
                "name": "Coast Starlight",
                "network": "Amtrak",
                "operator": "Amtrak",
                "public_transport:version": "1",
                "ref": "11-14",
                "route": "train",
                "service": "long_distance",
                "to": "Seattle",
                "type": "route",
                "via": "Portland"
            }),
        )

        self.assert_has_feature(
            5, 5, 11, 'transit',
            {'kind': 'train', 'service': 'long_distance'})

    def test_high_speed(self):
        self.generate_fixtures(dsl.way(895371274, wkt_loads('POINT (-73.99282355051621 40.7502330745949)'), {u'name:ko': u'\ud39c\uc2e4\ubca0\uc774\ub2c8\uc544 \uc5ed', u'wikidata': u'Q54451', u'alt_name': u'Pennsylvania Station', u'operator': u'Amtrak', u'name:ru': u'\u041f\u0435\u043d\u0441\u0438\u043b\u044c\u0432\u0430\u043d\u0441\u043a\u0438\u0439 \u0432\u043e\u043a\u0437\u0430\u043b', u'ref:Amtrak': u'NYP', u'addr:housenumber': u'234', u'network': u'New York City Subway', u'wikipedia': u'en:Pennsylvania Station (New York City)', u'addr:state': u'NY', u'source': u'openstreetmap.org', u'addr:street': u'West 31st Street', u'name:zh': u'\u8cd3\u5915\u6cd5\u5c3c\u4e9e\u8eca\u7ad9', u'name:he': u'\u05ea\u05d7\u05e0\u05ea \u05e4\u05e0\u05e1\u05d9\u05dc\u05d1\u05e0\u05d9\u05d4', u'name:ja': u'\u30da\u30f3\u30b7\u30eb\u30d9\u30cb\u30a2\u99c5', u'iata': u'ZYP', u'railway': u'station', u'addr:city': u'New York', u'name': u'New York Penn Station', u'addr:postcode': u'10001', u'wheelchair': u'yes', u'toilets:wheelchair': u'yes'}), dsl.way(5671507, wkt_loads('LINESTRING (-73.99746550491528 40.75218126681958, -73.998822410152 40.75275228020788)'), {u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'Northeast Corridor', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'tiger:reviewed': u'no', u'electrified': u'contact_line', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'frequency': u'25', u'voltage': u'12000', u'usage': u'main', u'gauge': u'1435', u'railway': u'rail', u'old_railway_operator': u'PRR', u'source': u'openstreetmap.org'}), dsl.way(32965981, wkt_loads('LINESTRING (-73.998822410152 40.75275228020788, -74.00390625 40.75498939123595)'), {u'layer': u'-2', u'tiger:name_base': u'Amtrak Railroad', u'name': u'Northeast Corridor', u'tiger:cfcc': u'B12', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'tiger:reviewed': u'no', u'designation': u'3', u'operator': u'Amtrak', u'electrified': u'contact_line', u'owner': u'Amtrak', u'frequency': u'25', u'gauge': u'1435', u'voltage': u'12000', u'usage': u'main', u'railway': u'rail', u'tiger:county': u'New York, NY', u'old_railway_operator': u'PRR'}), dsl.way(46493326, wkt_loads('LINESTRING (-73.99282355051621 40.7502330745949, -73.99746550491528 40.75218126681958)'), {u'layer': u'-1', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'wikipedia': u'en:Northeast Corridor', u'electrified': u'contact_line', u'operator': u'Amtrak', u'owner': u'Amtrak', u'frequency': u'25', u'gauge': u'1435', u'voltage': u'12000', u'usage': u'main', u'wikidata': u'Q678233', u'railway': u'rail', u'old_railway_operator': u'PRR'}), dsl.way(46493330, wkt_loads('LINESTRING (-73.98576272339383 40.7472569628042, -73.98954721501188 40.7488534902351)'), {u'layer': u'-1', u'name': u'Northeast Corridor', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'electrified': u'contact_line', u'operator': u'LIRR', u'owner': u'Amtrak', u'frequency': u'25', u'gauge': u'1435', u'voltage': u'12000', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'PRR'}), dsl.way(95579501, wkt_loads('LINESTRING (-73.99282355051621 40.7502330745949, -73.99092594931 40.7494361694018)'), {u'layer': u'-1', u'name': u'Northeast Corridor', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'electrified': u'contact_line', u'operator': u'Amtrak', u'owner': u'Amtrak', u'frequency': u'25', u'gauge': u'1435', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'PRR'}), dsl.way(350715090, wkt_loads('LINESTRING (-73.98954721501188 40.7488534902351, -73.99092594931 40.7494361694018)'), {u'layer': u'-1', u'name': u'Northeast Corridor', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'electrified': u'contact_line', u'operator': u'LIRR', u'owner': u'Amtrak', u'frequency': u'25', u'gauge': u'1435', u'voltage': u'12000', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'PRR'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.998822410152 40.75275228020788, -74.00390625 40.75498939123595)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.998822410152 40.75275228020788, -74.00390625 40.75498939123595)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.99746550491528 40.75218126681958, -73.998822410152 40.75275228020788)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train',
                               u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.99746550491528 40.75218126681958, -73.998822410152 40.75275228020788)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.99282355051621 40.7502330745949, -73.99746550491528 40.75218126681958)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.99282355051621 40.7502330745949, -73.99746550491528 40.75218126681958)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.99282355051621 40.7502330745949, -73.99092594931 40.7494361694018)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.99282355051621 40.7502330745949, -73.99092594931 40.7494361694018)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.98954721501188 40.7488534902351, -73.99092594931 40.7494361694018)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.98576272339383 40.7472569628042, -73.98954721501188 40.7488534902351)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}), dsl.way(-4460896, wkt_loads('LINESTRING (-73.98576272339383 40.7472569628042, -73.98954721501188 40.7488534902351)'), {u'passenger': u'national', u'FIXME': u'Underlying infrastructure "Northeast Corridor" needs some minor track connectivity fixes', u'via': u'New York Penn Station', u'from': u'Boston South Station', u'name': u'Acela Express', u'service': u'high_speed', u'route_pref_color': u'0', u'route': u'train', u'wikipedia': u'en:Acela Express', u'route_name': u'Acela Express', u'to': u'Washington Union Station', u'public_transport:version': u'1', u'wikidata': u'Q481759', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'2100-2297', u'colour': u'red'}))

        self.assert_has_feature(
            5, 9, 12, 'transit',
            {'kind': 'train', 'service': 'high_speed'})

    def test_international(self):
        self.generate_fixtures(dsl.way(895371274, wkt_loads('POINT (-73.99282355051621 40.7502330745949)'), {u'name:ko': u'\ud39c\uc2e4\ubca0\uc774\ub2c8\uc544 \uc5ed', u'wikidata': u'Q54451', u'alt_name': u'Pennsylvania Station', u'operator': u'Amtrak', u'name:ru': u'\u041f\u0435\u043d\u0441\u0438\u043b\u044c\u0432\u0430\u043d\u0441\u043a\u0438\u0439 \u0432\u043e\u043a\u0437\u0430\u043b', u'ref:Amtrak': u'NYP', u'addr:housenumber': u'234', u'network': u'New York City Subway', u'wikipedia': u'en:Pennsylvania Station (New York City)', u'addr:state': u'NY', u'source': u'openstreetmap.org', u'addr:street': u'West 31st Street', u'name:zh': u'\u8cd3\u5915\u6cd5\u5c3c\u4e9e\u8eca\u7ad9', u'name:he': u'\u05ea\u05d7\u05e0\u05ea \u05e4\u05e0\u05e1\u05d9\u05dc\u05d1\u05e0\u05d9\u05d4', u'name:ja': u'\u30da\u30f3\u30b7\u30eb\u30d9\u30cb\u30a2\u99c5', u'iata': u'ZYP', u'railway': u'station', u'addr:city': u'New York', u'name': u'New York Penn Station', u'addr:postcode': u'10001', u'wheelchair': u'yes', u'toilets:wheelchair': u'yes'}), dsl.way(46109424, wkt_loads('LINESTRING (-74.00216980239519 40.7557188033189, -74.00144558061308 40.7562063609175, -74.00116117399419 40.75631612042541, -73.9999328176747 40.75668996825098)'), {u'layer': u'-1', u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46481092, wkt_loads('LINESTRING (-74.00390625 40.75614321972709, -74.0028176673781 40.75568668495379, -74.0026548028171 40.75564469969457, -74.0025021790503 40.7556525931976, -74.00232718723301 40.75568396305769, -74.00216980239519 40.7557188033189)'), {u'layer': u'-1', u'name': u'West Side Line', u'tunnel': u'yes', u'source': u'openstreetmap.org', u'gauge': u'1435', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46481749, wkt_loads('LINESTRING (-73.9999328176747 40.75668996825098, -73.99961822766218 40.75683810504041, -73.99926222531511 40.75707599420548, -73.9986847882505 40.75763036247749, -73.99816789763599 40.7581528130875)'), {u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'electrified': u'yes', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46481750, wkt_loads('LINESTRING (-73.99816789763599 40.7581528130875, -73.99773868259318 40.75859156499908, -73.99682141285659 40.75944490467788, -73.9964673868031 40.75972531156949, -73.9960758111708 40.76003817377128, -73.99587189360129 40.76024951482548, -73.99559826676578 40.76063552010999)'), {u'layer': u'-1', u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46482605, wkt_loads('LINESTRING (-73.99434664408039 40.76238629436129, -73.9933662227793 40.76380778216978)'), {u'layer': u'-1', u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46482606, wkt_loads('LINESTRING (-73.9933662227793 40.76380778216978, -73.9930340257872 40.76429289909028)'), {u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46482608, wkt_loads('LINESTRING (-73.9930340257872 40.76429289909028, -73.9924633260872 40.7650394823503, -73.99210391014201 40.76555956145851, -73.99177126399229 40.7662380939251, -73.99147086736131 40.76692879788959, -73.99136899840811 40.76731877847799, -73.99111693113939 40.76863919820177, -73.99067702614478 40.7709672176864, -73.99048388835868 40.77177971599637, -73.9903349476846 40.77216517810169)'), {u'layer': u'-1', u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46482617, wkt_loads('LINESTRING (-73.99559826676578 40.76063552010999, -73.9952395694728 40.76113719434909)'), {u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46486240, wkt_loads('LINESTRING (-73.99897422543501 40.75253866964799, -74.00390625 40.75459628300685)'), {u'layer': u'-1', u'name': u'Empire Connection', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'operator': u'Amtrak', u'owner': u'Amtrak', u'gauge': u'1435', u'usage': u'main', u'railway': u'rail'}), dsl.way(46493327, wkt_loads('LINESTRING (-73.99761839817671 40.7519601687921, -73.99897422543501 40.75253866964799)'), {u'name': u'Empire Connection', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'operator': u'Amtrak', u'owner': u'Amtrak', u'gauge': u'1435', u'usage': u'main', u'railway': u'rail'}), dsl.way(46493329, wkt_loads('LINESTRING (-73.99092594931 40.7494361694018, -73.9911190870961 40.74947278233481, -73.99142738890158 40.74951449927659, -73.99192909798781 40.74958656812411, -73.992100676207 40.74962719613688, -73.993088733188 40.75004490783368, -73.99422914444121 40.75052706282669, -73.99761839817671 40.7519601687921)'), {u'layer': u'-1', u'source': u'openstreetmap.org', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'gauge': u'1435', u'usage': u'main', u'railway': u'rail'}), dsl.way(46526921, wkt_loads('LINESTRING (-73.98988587987398 40.77359557264391, -73.98977871086061 40.77478661485821, -73.9897099897414 40.77505961004577, -73.98957272716599 40.77535859053029, -73.98933242782751 40.77574205909349, -73.9890944641087 40.77603709096598, -73.9885795497879 40.77673177462759)'), {u'layer': u'-1', u'tiger:name_base': u'Metro North Commuter Railroad',
                               u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46526928, wkt_loads('LINESTRING (-73.989944180536 40.77329379502108, -73.98988587987398 40.77359557264391)'), {u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46526991, wkt_loads('LINESTRING (-73.9903349476846 40.77216517810169, -73.99029605063279 40.77237682074578)'), {u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(46526993, wkt_loads('LINESTRING (-73.99029605063279 40.77237682074578, -73.9899943963604 40.77312338121779, -73.989944180536 40.77329379502108)'), {u'layer': u'-1', u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(95181770, wkt_loads('LINESTRING (-73.9868039397973 40.78037956093689, -73.98673479488151 40.78054143186032)'), {u'layer': u'-1', u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(320902572, wkt_loads('LINESTRING (-73.99092594931 40.7494361694018, -73.9911190870961 40.74947278233481, -73.99142738890158 40.74951449927659, -73.99192909798781 40.74958656812411, -73.992100676207 40.74962719613688)'), {u'layer': u'-1', u'name': u'Empire Connection', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'source': u'openstreetmap.org', u'gauge': u'1435', u'owner': u'Amtrak', u'railway': u'rail'}), dsl.way(497193634, wkt_loads('LINESTRING (-73.9952395694728 40.76113719434909, -73.9946854886056 40.76191232225377)'), {u'layer': u'-1', u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'tunnel': u'yes', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(497193635, wkt_loads('LINESTRING (-73.9946854886056 40.76191232225377, -73.99434664408039 40.76238629436129)'), {u'tiger:name_base': u'Metro North Commuter Railroad', u'name': u'West Side Line', u'tiger:cfcc': u'B12', u'tiger:name_base_1': u'Amtrak Railroad', u'electrified': u'no', u'operator': u'Amtrak', u'owner': u'Amtrak', u'tiger:county': u'New York, NY', u'gauge': u'1435', u'source': u'openstreetmap.org', u'usage': u'main', u'railway': u'rail', u'old_railway_operator': u'NYC'}), dsl.way(-4467189, wkt_loads('MULTILINESTRING ((-73.992100676207 40.74962719613688, -73.99192909798781 40.74958656812411), (-73.99192909798781 40.74958656812411, -73.99142738890158 40.74951449927659), (-73.99142738890158 40.74951449927659, -73.9911190870961 40.74947278233481), (-73.9911190870961 40.74947278233481, -73.99092594931 40.7494361694018), (-73.992100676207 40.74962719613688, -73.993088733188 40.75004490783368, -73.99422914444121 40.75052706282669, -73.99761839817671 40.7519601687921, -73.99897422543501 40.75253866964799, -74.00390625 40.75459628300685), (-74.00390625 40.75614321972709, -74.0028176673781 40.75568668495379, -74.0026548028171 40.75564469969457, -74.0025021790503 40.7556525931976, -74.00232718723301 40.75568396305769, -74.00216980239519 40.7557188033189, -74.00144558061308 40.7562063609175, -74.00116117399419 40.75631612042541, -73.9999328176747 40.75668996825098, -73.99961822766218 40.75683810504041, -73.99926222531511 40.75707599420548, -73.9986847882505 40.75763036247749, -73.99816789763599 40.7581528130875, -73.99773868259318 40.75859156499908, -73.99682141285659 40.75944490467788, -73.9964673868031 40.75972531156949, -73.9960758111708 40.76003817377128, -73.99587189360129 40.76024951482548, -73.99559826676578 40.76063552010999, -73.9952395694728 40.76113719434909, -73.9946854886056 40.76191232225377, -73.99434664408039 40.76238629436129, -73.9933662227793 40.76380778216978, -73.9930340257872 40.76429289909028, -73.9924633260872 40.7650394823503, -73.99210391014201 40.76555956145851, -73.99177126399229 40.7662380939251, -73.99147086736131 40.76692879788959, -73.99136899840811 40.76731877847799, -73.99111693113939 40.76863919820177, -73.99067702614478 40.7709672176864, -73.99048388835868 40.77177971599637, -73.9903349476846 40.77216517810169, -73.99029605063279 40.77237682074578, -73.9899943963604 40.77312338121779, -73.989944180536 40.77329379502108, -73.98988587987398 40.77359557264391, -73.98977871086061 40.77478661485821, -73.9897099897414 40.77505961004577, -73.98957272716599 40.77535859053029, -73.98933242782751 40.77574205909349, -73.9890944641087 40.77603709096598, -73.9885795497879 40.77673177462759))'), {u'website': u'http://www.amtrak.com/', u'passenger': u'international', u'direction': u'north', u'from': u'New York, NY', u'name': u'Maple Leaf (Northbound)', u'service': u'international', u'route_pref_color': u'0', u'route': u'train', u'wheelchair': u'yes', u'wikipedia': u'en:Maple Leaf (train)', u'route_name': u'Maple Leaf (Northbound)', u'to': u'Toronto, ON', u'public_transport:version': u'2', u'wikidata': u'Q592407', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'63', u'colour': u'indigo', u'network': u'Amtrak'}), dsl.way(-4467189, wkt_loads('LINESTRING (-73.9868039397973 40.78037956093689, -73.98673479488151 40.78054143186032)'), {u'website': u'http://www.amtrak.com/', u'passenger': u'international', u'direction': u'north', u'from': u'New York, NY', u'name': u'Maple Leaf (Northbound)', u'service': u'international', u'route_pref_color': u'0', u'route': u'train', u'wheelchair': u'yes', u'wikipedia': u'en:Maple Leaf (train)', u'route_name': u'Maple Leaf (Northbound)', u'to': u'Toronto, ON', u'public_transport:version': u'2', u'wikidata': u'Q592407', u'source': u'openstreetmap.org', u'operator': u'Amtrak', u'ref': u'63', u'colour': u'indigo', u'network': u'Amtrak'}))

        self.assert_has_feature(
            5, 9, 12, 'transit',
            {'kind': 'train', 'service': 'international'})
