-- These fill in the gaps caused by several missing ways along Aurora Ave in Seattle in Daylight 1.15

-- way 8591493
update planet_osm_line
set way = st_geometryfromtext('LineString (-13619633.12467937543988228 6049279.65133139304816723, -13619631.32130362465977669 6049506.8966157054528594, -13619632.42336658574640751 6049588.83264238853007555, -13619633.04675573110580444 6049635.17195791471749544, -13619634.13768674246966839 6049716.00193730648607016, -13619633.15807522274553776 6049923.34396426193416119, -13619633.12467937543988228 6049951.40641953889280558, -13619633.04675573110580444 6050016.2908675679937005, -13619632.99109598807990551 6050065.73955697193741798, -13619632.9465681929141283 6050103.6030330928042531, -13619634.2044784389436245 6050257.30632273852825165, -13619634.37145767547190189 6050285.96485182363539934, -13619634.26013818383216858 6050405.78960587084293365, -13619634.31579792685806751 6050437.4236185634508729, -13619634.66088834963738918 6050570.60507556796073914, -13619634.82786758616566658 6050586.07528126612305641)')
where osm_id = 8591493;

-- way 338894965
update planet_osm_line
set way = st_geometryfromtext('LineString (-13619651.60371484979987144 6050599.95882281567901373, -13619651.38107586838304996 6050519.93042933195829391, -13619651.28088832460343838 6050482.2634601229801774, -13619650.80221451632678509 6050364.81761655956506729, -13619649.47751257382333279 6050252.19936301372945309, -13619649.95618638582527637 6050159.92753368522971869, -13619650.3012768067419529 6050103.95010195393115282, -13619651.93767332099378109 6049925.82297607138752937, -13619648.65374834276735783 6049712.59751071780920029, -13619647.87451190687716007 6049633.3044985169544816, -13619646.64999750815331936 6049508.02038007136434317)')
where osm_id = 338894965;



