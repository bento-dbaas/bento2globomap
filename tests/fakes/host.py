HOST_API_PAGE_1 = {
  "_links": {
    "count": 1499,
    "self": "https://dbaas.globoi.com/api/host/?format=json",
    "previous": None,
    "next": "https://dbaas.globoi.com/api/host/?page=2&format=json"
  },
  "host": [{
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8666,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-18T15:07:08",
    "created_at": "2018-01-18T15:03:53",
    "team_name": "dbaas",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "fake_hostname1",
    "identifier": "fake_identifier1",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": "DBaaS",
      "name": "bento2globomap",
      "infra": {
        "id": 4202,
        "name": "fake_infra_name1"
      },
      "id": 3357
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8665,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-18T15:07:00",
    "created_at": "2018-01-18T15:03:31",
    "team_name": "dbaas",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "fake_hostname2",
    "identifier": "fake_identifier2",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23725",
      "used": None
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": "DBaaS",
      "name": "bento2globomap",
      "infra": {
        "id": 4202,
        "name": "fake_infra_name2"
      },
      "id": 3357
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8664,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-18T15:04:32",
    "created_at": "2018-01-18T15:02:58",
    "team_name": "dbaas",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "bento2glob-01-151629495609.globoi.com",
    "identifier": "b145775f-d2a2-4b76-b778-32c7fc8d06b5",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23724",
      "used": None
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": "DBaaS",
      "name": "bento2globomap",
      "infra": {
        "id": 4202,
        "name": "bento2glob151629495609"
      },
      "id": 3357
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8663,
    "os_description": "Red Hat Enterprise Linux Server release 6.6 (Santiago)",
    "updated_at": "2018-01-18T12:03:36",
    "created_at": "2018-01-18T12:01:07",
    "team_name": "Storm",
    "env_name": "prod",
    "region_name": "rjcme",
    "hostname": "custeio-03-151628396512.globoi.com",
    "identifier": "a9de1cbb-a2cd-4eb6-ba82-916ad614e8b8",
    "offering": {
      "type": "1c2048",
      "cpus": 1,
      "memory": 2048
    },
    "disks": [],
    "project_id": "431fe0ef-0d34-49f0-b7da-f303ffd9c676",
    "database": {
      "engine": "mongodb_3.4.1",
      "project_name": "Custeio",
      "name": "custeio",
      "infra": {
        "id": 4201,
        "name": "custeio151628396512"
      },
      "id": 3356
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8662,
    "os_description": "Red Hat Enterprise Linux Server release 6.6 (Santiago)",
    "updated_at": "2018-01-18T12:02:58",
    "created_at": "2018-01-18T12:00:34",
    "team_name": "Storm",
    "env_name": "prod",
    "region_name": "rjcme",
    "hostname": "custeio-02-151628396512.globoi.com",
    "identifier": "fa50a826-4227-4bd3-9e9c-4c7bef71fd70",
    "offering": {
      "type": "2c4096",
      "cpus": 2,
      "memory": 4096
    },
    "disks": [{
      "active": True,
      "total": 20971520,
      "export_id": "23717",
      "used": None
    }],
    "project_id": "431fe0ef-0d34-49f0-b7da-f303ffd9c676",
    "database": {
      "engine": "mongodb_3.4.1",
      "project_name": "Custeio",
      "name": "custeio",
      "infra": {
        "id": 4201,
        "name": "custeio151628396512"
      },
      "id": 3356
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8661,
    "os_description": "Red Hat Enterprise Linux Server release 6.6 (Santiago)",
    "updated_at": "2018-01-18T12:01:51",
    "created_at": "2018-01-18T11:59:57",
    "team_name": "Storm",
    "env_name": "prod",
    "region_name": "rjcme",
    "hostname": "custeio-01-151628396512.globoi.com",
    "identifier": "d2a0bd70-c127-4848-8fee-6f36f5b2f9fe",
    "offering": {
      "type": "2c4096",
      "cpus": 2,
      "memory": 4096
    },
    "disks": [{
      "active": True,
      "total": 20971520,
      "export_id": "23716",
      "used": None
    }],
    "project_id": "431fe0ef-0d34-49f0-b7da-f303ffd9c676",
    "database": {
      "engine": "mongodb_3.4.1",
      "project_name": "Custeio",
      "name": "custeio",
      "infra": {
        "id": 4201,
        "name": "custeio151628396512"
      },
      "id": 3356
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8660,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-18T11:14:24",
    "created_at": "2018-01-18T11:11:53",
    "team_name": "Backoffice",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "hackdayzab-01-15162810714.globoi.com",
    "identifier": "5e72a4ae-f714-4723-9a3b-ad7bfed0b783",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23709",
      "used": None
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "mysql_5.6.24",
      "project_name": None,
      "name": "hackday_zabbix_mysql_dev",
      "infra": {
        "id": 4200,
        "name": "hackdayzab15162810714"
      },
      "id": 3355
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8659,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-17T15:09:26",
    "created_at": "2018-01-17T15:07:36",
    "team_name": "bigdata",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "datascienc-01-151620883472.globoi.com",
    "identifier": "79379b41-d3f6-4669-849e-957e25c34fda",
    "offering": {
      "type": "1c512",
      "cpus": 1,
      "memory": 512
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23686",
      "used": 64
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": "Ambiente Datascience",
      "name": "datascienceredis",
      "infra": {
        "id": 4199,
        "name": "datascienc151620883472"
      },
      "id": 3354
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8657,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-16T09:39:42",
    "team_name": "gg_infoedg_apps",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "redisiluva-01-151610275839.globoi.com",
    "identifier": "13d6dabd-e089-4f79-ab14-69da9251d524",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23667",
      "used": 256
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": None,
      "name": "redis_iluvatar_dev",
      "infra": {
        "id": 4197,
        "name": "redisiluva151610275839"
      },
      "id": 3352
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json"
    },
    "id": 8656,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-16T09:27:55",
    "team_name": "gg_infoedg_apps",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "mysqlragna-01-151610205422.globoi.com",
    "identifier": "50e6bbc7-8941-44f7-aabf-01f551fc3de7",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23666",
      "used": 172224
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "mysql_5.6.24",
      "project_name": None,
      "name": "mysql_ragnarok_dev2",
      "infra": {
        "id": 4196,
        "name": "mysqlragna151610205422"
      },
      "id": 3351
    }
  }]
}

HOST_API_PAGE_2 = {
  "_links": {
    "count": 1499,
    "self": "https://dbaas.globoi.com/api/host/?format=json&page=2",
    "previous": "https://dbaas.globoi.com/api/host/?page=1&format=json",
    "next": None
  },
  "host": [{
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8655,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-15T17:52:04",
    "team_name": "globoservico",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "fake_hostname1_page2",
    "identifier": "fake_identifier1_page2",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23665",
      "used": 703552
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "mysql_5.6.24",
      "project_name": None,
      "name": "gsdata_dev",
      "infra": {
        "id": 4195,
        "name": "fake_infra_name1_page2"
      },
      "id": 3350
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8654,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-15T17:40:33",
    "team_name": "bigdata",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "bigdataazk-01-151604519155.globoi.com",
    "identifier": "a2f30cb1-5752-4b28-a549-945ae416b1de",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23664",
      "used": 172672
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "mysql_5.6.24",
      "project_name": "Big Data Cluster",
      "name": "bigdata_azkaban_qa",
      "infra": {
        "id": 4194,
        "name": "bigdataazk151604519155"
      },
      "id": 3349
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8653,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-15T17:37:12",
    "team_name": "globoservico",
    "env_name": "qa2",
    "region_name": "rjdev qa2",
    "hostname": "gsdatahomo-01-151604500959.globoi.com",
    "identifier": "d47a370c-d1e2-4b28-960d-04cac7609f48",
    "offering": {
      "type": "1c512",
      "cpus": 1,
      "memory": 512
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23663",
      "used": 692544
    }],
    "project_id": "59fbc722-1ad0-4b17-9f07-6a37fa473a3c",
    "database": {
      "engine": "mysql_5.6.24",
      "project_name": None,
      "name": "gsdata_homolog",
      "infra": {
        "id": 4193,
        "name": "gsdatahomo151604500959"
      },
      "id": 3348
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8652,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-15T17:22:56",
    "team_name": "bigdata",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "azkaban-01-151604415262.globoi.com",
    "identifier": "e863687e-a249-4ac8-ba1f-292dfdca854c",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23662",
      "used": 168832
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "mysql_5.6.24",
      "project_name": "Big Data Cluster",
      "name": "azkaban",
      "infra": {
        "id": 4192,
        "name": "azkaban151604415262"
      },
      "id": 3347
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8649,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-15T16:17:48",
    "team_name": "blackbird",
    "env_name": "prod",
    "region_name": "rjcme",
    "hostname": "xavierstgr-03-151604017312.globoi.com",
    "identifier": "d3aebf43-058a-4dab-bb5c-3ed24ea949d2",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [],
    "project_id": "431fe0ef-0d34-49f0-b7da-f303ffd9c676",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": None,
      "name": "xavier_stg_redis_dbaas",
      "infra": {
        "id": 4190,
        "name": "xavierstgr151604017312"
      },
      "id": 3346
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8648,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-15T16:17:16",
    "team_name": "blackbird",
    "env_name": "prod",
    "region_name": "rjcme",
    "hostname": "xavierstgr-02-151604017312.globoi.com",
    "identifier": "37af218e-c6a4-4cf9-8c46-1c368f6c52a7",
    "offering": {
      "type": "2c4096",
      "cpus": 2,
      "memory": 4096
    },
    "disks": [{
      "active": True,
      "total": 20971520,
      "export_id": "23660",
      "used": 0
    }],
    "project_id": "431fe0ef-0d34-49f0-b7da-f303ffd9c676",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": None,
      "name": "xavier_stg_redis_dbaas",
      "infra": {
        "id": 4190,
        "name": "xavierstgr151604017312"
      },
      "id": 3346
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8647,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-15T16:16:45",
    "team_name": "blackbird",
    "env_name": "prod",
    "region_name": "rjcme",
    "hostname": "xavierstgr-01-151604017312.globoi.com",
    "identifier": "06e90e68-3419-4af4-9d91-0a5999e29774",
    "offering": {
      "type": "2c4096",
      "cpus": 2,
      "memory": 4096
    },
    "disks": [{
      "active": True,
      "total": 20971520,
      "export_id": "23659",
      "used": 0
    }],
    "project_id": "431fe0ef-0d34-49f0-b7da-f303ffd9c676",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": None,
      "name": "xavier_stg_redis_dbaas",
      "infra": {
        "id": 4190,
        "name": "xavierstgr151604017312"
      },
      "id": 3346
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8646,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:55",
    "created_at": "2018-01-15T12:14:31",
    "team_name": "Seguranca",
    "env_name": "qa2",
    "region_name": "rjdev qa2",
    "hostname": "aclapiqa2-01-15160256491.globoi.com",
    "identifier": "9de22f50-0717-415f-9cae-80cded575e4c",
    "offering": {
      "type": "1c512",
      "cpus": 1,
      "memory": 512
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23655",
      "used": 462144
    }],
    "project_id": "59fbc722-1ad0-4b17-9f07-6a37fa473a3c",
    "database": {
      "engine": "mysql_5.6.24",
      "project_name": "ACL_API",
      "name": "acl_api_qa2",
      "infra": {
        "id": 4188,
        "name": "aclapiqa215160256491"
      },
      "id": 3345
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8645,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:54",
    "created_at": "2018-01-12T18:11:24",
    "team_name": "appdev",
    "env_name": "dev",
    "region_name": "rjdev",
    "hostname": "backstageg-01-151578786291.globoi.com",
    "identifier": "89a2f110-2034-4574-8043-c021311703b6",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [{
      "active": True,
      "total": 2097152,
      "export_id": "23652",
      "used": 169920
    }],
    "project_id": "7c0d5672-04ee-4502-82b3-34d4ac76ac51",
    "database": {
      "engine": "mysql_5.6.24",
      "project_name": None,
      "name": "backstage_gateway_admin_qa01_02",
      "infra": {
        "id": 4187,
        "name": "backstageg151578786291"
      },
      "id": 3344
    }
  }, {
    "_links": {
      "self": "https://dbaas.globoi.com/api/host/?format=json&page=2"
    },
    "id": 8643,
    "os_description": "Red Hat Enterprise Linux Server release 6.9 (Santiago)",
    "updated_at": "2018-01-16T16:30:54",
    "created_at": "2018-01-12T12:34:31",
    "team_name": "globoid",
    "env_name": "prod",
    "region_name": "rjcme",
    "hostname": "gliveuserc-03-151576759584.globoi.com",
    "identifier": "b9f365eb-2eb7-4e7a-9dca-4fea7890071a",
    "offering": {
      "type": "1c1024",
      "cpus": 1,
      "memory": 1024
    },
    "disks": [],
    "project_id": "431fe0ef-0d34-49f0-b7da-f303ffd9c676",
    "database": {
      "engine": "redis_3.2.6",
      "project_name": "Glive",
      "name": "glive_user_cache_prd",
      "infra": {
        "id": 4185,
        "name": "gliveuserc151576759584"
      },
      "id": 3343
    }
  }]
}
