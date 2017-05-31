import settings
import boto3

def get_memcached_instances():
    memcached_instances = {}
    client = boto3.client('elasticache')
    response = client.describe_cache_clusters(MaxRecords=100)
    for cluster in response["CacheClusters"]:
        if cluster['Engine'] == 'memcached':
            memcached_instances[cluster['CacheClusterId']] = cluster['ConfigurationEndpoint']
    return memcached_instances

def get_redis_replication_groups():
    replication_groups = {}
    client = boto3.client('elasticache')
    response = client.describe_replication_groups(MaxRecords=100)
    for group in response["ReplicationGroups"]:
        replication_groups[group["ReplicationGroupId"]] = group["NodeGroups"][0]["PrimaryEndpoint"]
    return replication_groups


def collect_elasticache_information():
    elasticache_information = {}
    elasticache_information.update(get_redis_replication_groups())
    elasticache_information.update(get_memcached_instances())
    return elasticache_information
