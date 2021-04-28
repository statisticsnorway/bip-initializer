def required_input():
    required_input = """{
            "name": "am-hello-world",
            "namespace": "stratus",
            "flux_image_tag_pattern" : "glob:main-*",
            "cluster": "staging-bip-app",
            "billingproject": "ssb-stratus",
            "image_repository": "eu.gcr.io/prod-bip/ssb/stratus/am-hello-world",
            "image_tag": "main-d2193bee3f24ae19e04d77826079d02cf58c0514",
            "port": 5000,
            "apptype": "backend",
            "exposed": true,
            "authentication": true
        }"""
    return required_input
