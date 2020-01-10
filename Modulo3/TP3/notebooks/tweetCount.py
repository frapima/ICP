#!/usr/bin/env python
# coding: utf-8

# # TP3 - Apartado 2 - Infraestructuras Computacionales para el Procesamiento de Datos Masivos
# ## Ejercicio 1
# ### [Enunciado]

# In[ ]:


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


# In[ ]:


sc = SparkContext("local[4]")
ssc = StreamingContext(sc, batchDuration = 1)


# In[ ]:


dstream = KafkaUtils.createDirectStream(
    ssc, 
    topics = ['kafkaTwitter'],
    kafkaParams = {
        'bootstrap.servers' : 'localhost:9092'
    })


# In[ ]:


ssc.start()

