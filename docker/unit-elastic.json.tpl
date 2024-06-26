{
    "listeners": {
        "*:5000": {
            "pass": "applications/hapi"
        }
    },
    "applications": {
        "hapi": {
            "type": "python 3.12",
            "threads": 1,
            "processes": {
                "max": ${UNITD_MAX_WORKERS},
                "spare": 3,
                "idle_timeout": 20
            },
            "environment": {
                "HOME": "/srv/hapi"
            },
            "path": "/srv/hapi",
            "module": "main_elastic",
            "callable": "app"
        }
    },
    "settings": {
        "http": {
            "max_body_size": 1584000000
        }
    }
}
