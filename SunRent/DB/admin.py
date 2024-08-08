from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from .models import*

# admin.site.register(Scooter)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(User)
admin.site.register(Mission)

@admin.register(Polygon)
class PolygonAdmin(geoadmin.GISModelAdmin):
    list_display = ('name', 'area')
    map_template = 'gis/admin/openlayers.html'
    map_width = 1000
    map_height = 1000
    wms_url = 'https://ows.terrestris.de/osm/service'
    wms_layer = 'OSM-WMS'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['start_lat'] = 42.857026  # Центр карты (широта)
        extra_context['start_lon'] = 74.61006  # Центр карты (долгота)
        extra_context['default_zoom'] = 16  # Уровень зума по умолчанию
        return super().changelist_view(request, extra_context=extra_context)
    
@admin.register(Loscation)
class PolygonAdmin(geoadmin.GISModelAdmin):
    list_display = ('name', 'area')
    map_template = 'gis/admin/openlayers.html'
    map_width = 1000
    map_height = 1000
    wms_url = 'https://ows.terrestris.de/osm/service'
    wms_layer = 'OSM-WMS'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['start_lat'] = 42.857026  # Центр карты (широта)
        extra_context['start_lon'] = 74.61006  # Центр карты (долгота)
        extra_context['default_zoom'] = 16  # Уровень зума по умолчанию
        return super().changelist_view(request, extra_context=extra_context)
    
@admin.register(Scooter)
class Polygon_Scooter(geoadmin.GISModelAdmin):
    list_display = ('identifier', 'location', 'battery_percentage', 'polygon')
    map_template = 'gis/admin/openlayers.html'
    map_width = 1000
    map_height = 1000
    wms_url = 'https://ows.terrestris.de/osm/service'
    wms_layer = 'OSM-WMS'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['start_lat'] = 42.857026  # Центр карты (широта)
        extra_context['start_lon'] = 74.61006  # Центр карты (долгота)
        extra_context['default_zoom'] = 16  # Уровень зума по умолчанию
        return super().changelist_view(request, extra_context=extra_context)
