from extras.plugins import PluginMenuItem
from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

rplist_buttons = [
    PluginMenuButton(
        link="plugins:netbox_rp_mapping:staticrp_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
    )
]

rpgroup_buttons = [
    PluginMenuButton(
        link="plugins:netbox_rp_mapping:rpgroupentry_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_rp_mapping:staticrp_list",
        link_text="Static RPs",
        buttons=rplist_buttons,
    ),
    PluginMenuItem(
        link="plugins:netbox_rp_mapping:rpgroupentry_list",
        link_text="Multicast Groups",
        buttons=rpgroup_buttons,
    ),
)
