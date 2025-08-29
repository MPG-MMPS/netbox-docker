# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

PLUGINS = [
    "netbox_qrcode",
    "netbox_floorplan",
    "netbox_lifecycle",
    "netbox_topology_views",
    "netbox_reorder_rack",
    "netbox_interface_synchronization",
    "netbox_diode_plugin",
]


PLUGINS_CONFIG = {
    "netbox_topology_views": {"allow_coordinates_saving": True},
    "netbox_qrcode": {
        "rack": {
            "label_height": "24mm",
            "label_width": "95mm",
            "label_edge_left": "2mm",
            "label_edge_right": "2mm",
            "label_qr_height": "18mm",
            "label_qr_width": "18mm",
            "label_qr_text_distance": "5mm",
            "text_align_horizontal": "center",
            "font_size": "12.0mm",
            "font_weight": "bold",
        },
        "cable": {
            "with_qr": False,
            "label_height": "24mm",
            "label_width": "90mm",
            "label_edge_left": "5.0mm",
            "label_edge_right": "0.0mm",
            "label_edge_top": "0.0mm",
            "font_size": "3.0mm",
            "text_align_vertical": "middle",
            "text_align_horizontal": "center",
            "text_template": '<span style="writing-mode: vertical-lr; transform: scale(-1);">'
            "{{ obj.id }}</br>"
            "{{ obj.label }}</br>"
            "{{ obj.id }}</br>"
            "{{ obj.label }}</br>"
            "{{ obj.id }}</br>"
            "{{ obj.label }}</br>"
            "{{ obj.id }}</br>"
            "{{ obj.label }}</br>"
            "{{ obj.id }}</br>"
            "{{ obj.label }}</br>"
            "{{ obj.id }}</br>"
            "{{ obj.label }}</br>"
            "</span>",
        },
        "powerfeed": {
            "with_qr": False,
            "label_height": "24mm",
            "label_width": "95mm",
            "text_align_horizontal": "center",
            "font_size": "12.0mm",
            "font_weight": "bold",
        },
    },
}
