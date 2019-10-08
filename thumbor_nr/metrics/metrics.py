import newrelic.agent
from thumbor.metrics import BaseMetrics

newrelic.agent.initialize('/some/path/newrelic.ini', 'staging')
newrelic.agent.record_custom_metric(name, value, application=None)


    @classmethod
    def client(cls, config):
        """
        Cache statsd client so it doesn't do a DNS lookup
        over and over
        """
        if not hasattr(cls, "_client"):
            cls._client = newrelic.agent.initialize('/some/path/newrelic.ini', 'staging')
        return cls._client

    def incr(self, metricname, value=1):
        Metrics.client(self.config).record_custom_metric((name, value, application=None)

    #def timing(self, metricname, value):
    #    Metrics.client(self.config).timing(metricname, value)
 @classmethod

