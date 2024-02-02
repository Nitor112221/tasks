import sys
from Samples.geocoder import get_coordinates, get_ll_span
from Samples.mapapi_PG import show_map

t_t_f = ' '.join(sys.argv[1:])
if t_t_f:
    lat, lon = get_coordinates(t_t_f)
    ll_spn = f'll={lat},{lon}&spn=0.005,0.005'
    show_map(ll_spn, 'map')

    ll, spn = get_ll_span(t_t_f)
    ll_spn = f'll={ll}&spn={spn}'
    show_map(ll_spn, 'map')

    point_param = f'pt={ll}'
    show_map(ll_spn, 'map', add_params=point_param)
else:
    print('Данных нет :(')
