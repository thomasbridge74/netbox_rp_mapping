from extras.plugins import PluginConfig


class NetBoxRpMappingsConfig(PluginConfig):
    name = "netbox_rp_mapping"
    verbose_name = "NetBox RP Mapping"
    description = "Manage static RP Maps in NetBox"
    version = "0.1"
    base_url = "rp-mapping"
    author = "Thomas Bridge"
    author_email = "thomas.bridge@icloud.com"


config = NetBoxRpMappingsConfig
