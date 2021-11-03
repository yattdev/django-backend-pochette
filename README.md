# django-backend-pochette
A RESTFUL API DJANGO to manage music album covers 

# TEST COVERAGE
Name                                                                        Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------------------------------------
api/__init__.py                                                                 0      0   100%
api/admin.py                                                                    1      0   100%
api/apps.py                                                                     3      0   100%
api/migrations/__init__.py                                                      0      0   100%
api/models.py                                                                   1      0   100%
api/permissions.py                                                              6      1    83%   11
api/serializers/__init__.py                                                     0      0   100%
api/serializers/pochette.py                                                     8      0   100%
api/serializers/users.py                                                       22      2    91%   35-39
api/tests/__init__.py                                                           0      0   100%
api/tests/test_gp_endpoints.py                                                 39      2    95%   67-71
api/tests/test_gp_serializers.py                                                1      0   100%
api/tests/test_users_serializers.py                                             1      0   100%
api/urls.py                                                                     3      0   100%
api/views.py                                                                   39     10    74%   34, 41-56, 73-75
backend/__init__.py                                                             0      0   100%
backend/settings.py                                                            59     13    78%   34, 175-197
backend/urls.py                                                                15      1    93%   56
gestion_prochette/__init__.py                                                   0      0   100%
gestion_prochette/admin.py                                                      6      0   100%
gestion_prochette/apps.py                                                       3      0   100%
gestion_prochette/migrations/0001_initial.py                                    9      0   100%
gestion_prochette/migrations/0002_auto_20211103_0053.py                         5      0   100%
gestion_prochette/migrations/0003_auto_20211103_0105.py                         5      0   100%
gestion_prochette/migrations/0004_alter_pochette_image_for_detail_page.py       5      0   100%
gestion_prochette/migrations/0005_alter_pochette_image_for_detail_page.py       5      0   100%
gestion_prochette/migrations/0006_alter_pochette_image_for_detail_page.py       5      0   100%
gestion_prochette/migrations/0007_alter_pochette_image_for_detail_page.py       4      0   100%
gestion_prochette/migrations/0008_alter_pochette_image_for_detail_page.py       5      0   100%
gestion_prochette/migrations/0009_alter_pochette_image_for_detail_page.py       5      0   100%
gestion_prochette/migrations/0010_auto_20211103_0204.py                         5      0   100%
gestion_prochette/migrations/__init__.py                                        0      0   100%
gestion_prochette/models.py                                                    16      1    94%   44
gestion_prochette/tests/__init__.py                                             0      0   100%
gestion_prochette/tests/tests_models.py                                        23      0   100%
manage.py                                                                       9      2    78%   9-10
users/__init__.py                                                               0      0   100%
users/admin.py                                                                  8      0   100%
users/apps.py                                                                   4      0   100%
users/migrations/0001_initial.py                                                8      0   100%
users/migrations/__init__.py                                                    0      0   100%
users/models.py                                                                18      0   100%
users/tests/__init__.py                                                         0      0   100%
users/tests/test_models.py                                                     53      0   100%
---------------------------------------------------------------------------------------------------------
TOTAL                                                                         399     32    92%
