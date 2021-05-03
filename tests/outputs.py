def required_output():
    required_output = """
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
      "exposed": "True",
      "istioEndUserAuth": {
        "enabled": "True"
      },
      "billingProject": "ssb-stratus",
      "image": {
        "repository": "eu.gcr.io/prod-bip/ssb/stratus/am-hello-world",
        "tag": "main-d2193bee3f24ae19e04d77826079d02cf58c0514"
      },
      "port": {
        "name": "http-am-hello-world",
        "containerport": 5000
      },
      "probes": {
        "liveness": {
          "enabled": "True",
          "livenessProbe": {
            "httpGet": {
              "port": 5000,
              "path": "/health/alive"
            }
          }
        },
        "readiness": {
          "enabled": "True",
          "readinessProbe": {
            "httpGet": {
              "port": 5000,
              "path": "/health/ready"
            }
          }
        }
      },
      "metrics": {
        "enabled": "True",
        "path": "/metrics",
        "port": 5000
      }
    }
  }
}
            """

    return required_output
