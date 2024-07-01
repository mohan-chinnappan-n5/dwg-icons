# icon_definitions.py

from diagrams.custom import Custom

def get_icons():
    # Define the icons as Custom nodes
    sf_icon = "sf.svg.png"
    mulesoft_icon = "mulesoft.svg.png"

    sf_st = Custom("ST", sf_icon)
    sf_sit = Custom("SIT", sf_icon)
    sf_uat = Custom("UAT", sf_icon)
    sf_staging = Custom("Staging", sf_icon)
    sf_PROD = Custom("Production", sf_icon)

    dev_int = Custom("DEV_INT", mulesoft_icon)
    QA_int = Custom("QA_INT", mulesoft_icon)
    PROD_int = Custom("PROD_INT", mulesoft_icon)

    return sf_st, sf_sit, sf_uat, sf_staging, sf_PROD, dev_int, QA_int, PROD_int
