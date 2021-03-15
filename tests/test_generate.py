import json


def test_generate(client):
    post_data = """{
            "name": "am-hello-world",
            "namespace": "stratus",
            "flux_image_tag_pattern" : "glob:main-*",
            "cluster": "staging-bip-app",
            "billingproject": "ssb-stratus",
            "image_repository": "eu.gcr.io/prod-bip/ssb/stratus/am-hello-world",
            "image_tag": "main-d2193bee3f24ae19e04d77826079d02cf58c0514",
            "port": 5000,
            "apptype": "backend",
            "exposed": false
        }"""
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=json.loads(post_data),
    )
    assert response.status_code == 200
    expected_result = """
         {
           "apiVersion": "helm.fluxcd.io/v1",
           "kind": "HelmRelease",
           "metadata": {
             "name": "am-hello-world",
             "namespace": "stratus",
             "annotations": {
               "fluxcd.io/ignore": "false",
               "fluxcd.io/automated": "true",
               "fluxcd.io/tag.chart-image": "glob:main-*",
               "fluxcd.io/locked": "false"
             }
           },
           "spec": {
             "chart": {
               "git": "ssh://git@github.com/statisticsnorway/platform-dev",
               "ref": "master",
               "path": "helm/charts/ssb-chart"
             },
             "releaseName": "am-hello-world",
             "helmVersion": "v3",
             "values": {
               "name": "am-hello-world",
               "appType": "backend",
               "cluster": "staging-bip-app",
               "exposed": false,
               "billingProject": "ssb-stratus",
               "image": {
                 "repository": "eu.gcr.io/prod-bip/ssb/stratus/am-hello-world",
                 "tag": "main-d2193bee3f24ae19e04d77826079d02cf58c0514"
               },
               "port": {
                 "name": "http-am-hello-world",
                 "containerport": 5000
               }
             }
           }
         }
        """
    assert response.json() == json.loads(expected_result)


def test_wrong_type(client):
    post_data = """{
              "name": "am-hello-world",
              "namespace": "stratus",
              "flux_image_tag_pattern" : "glob:main-*",
              "cluster": "staging-bip-app",
              "billingproject": "ssb-stratus",
              "image_repository": "eu.gcr.io/prod-bip/ssb/stratus/am-hello-world",
              "image_tag": "main-d2193bee3f24ae19e04d77826079d02cf58c0514",
              "port": "Femhundre",
              "apptype": "backend",
              "exposed": false
          }"""
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=json.loads(post_data),
    )
    assert response.status_code == 422


def test_missing_value(client):
    post_data = """{
              "name": "am-hello-world",
              "namespace": "stratus",
              "flux_image_tag_pattern" : "glob:main-*",
              "billingproject": "ssb-stratus",
              "image_repository": "eu.gcr.io/prod-bip/ssb/stratus/am-hello-world",
              "image_tag": "main-d2193bee3f24ae19e04d77826079d02cf58c0514",
              "port": 5000,
              "apptype": "backend",
              "exposed": false
          }"""
    response = client.post(
        "/api/v1/generate",
        headers={"Content-Type": "application/json"},
        json=json.loads(post_data),
    )
    assert response.status_code == 422
