**Introdution**

Apache Spark is a lightning fast real-time processing framework. 
It does in-memory computations to analyze data in real-time. 
It came into picture as Apache Hadoop MapReduce was performing batch processing only and lacked a real-time processing feature. 
Hence, Apache Spark was introduced as it can perform stream processing in real-time and can also take care of batch processing.

Apache Spark is written in Scala programming language. To support Python with Spark, Apache Spark Community released a tool, PySpark. Using PySpark, you can work with RDDs in Python programming language also. It is because of a library called Py4j that they are able to achieve this.

PySpark offers PySpark Shell which links the Python API to the spark core and initializes the Spark context. Majority of data scientists and analytics experts today use Python because of its rich library set. Integrating Python with Spark is a boon to them.

SparkContext is the entry point to any spark functionality. When we run any Spark application, a driver program starts, which has the main function and your SparkContext gets initiated here. The driver program then runs the operations inside the executors on worker nodes.

SparkContext uses Py4J to launch a JVM and creates a JavaSparkContext. By default, PySpark has SparkContext available as 'sc', so creating a new SparkContext won't work.

**RDD**

RDD stands for Resilient Distributed Dataset, these are the elements that run and operate on multiple nodes to do parallel processing on a cluster. RDDs are immutable elements(create RDD,cannot change it)
RDDs are fault tolerant(in case of any failure, they recover automatically)
You can apply mutliple operations on these RDDs to achieve a certain task.

To apply operations on these RDD's, there are two ways 
 - Transformation
 - Action
Transformation - these are the operations, which are applied on a RDD to create a new RDD.
(for example filter, groupBy, map)
Action - these are the operations that are applied on RDD, which instructs Spark to perform computation and send the result back to the driver.

**Broadcast&accumulator**

For parallel processing, Apache Spark uses shared variables. A copy of shared variable goes on each node of the cluster when the driver sends a task to the executor on the cluster, so that it can be used for performing tasks.
There are two types of shared variables supported by Apache Spark
 - Broadcast
 - Accumulator
Broadcast variables are used to save the copy of data across all nodes. This variable is cached on all the machines and not sent on machines with tasks.

Accumulator variables are used for aggregating the information through aasociative and commutative operations. For example, we can use an accumulator for a sum ooperation or counters.
An Accumulator variable has an attribute called value that is similar to what a broadcast variable has. It stores the data used to return the accumulator's value, but usable only in a driver program.

**SparkConf**

To run a Spark application on the local/cluster, you need to set a few configurations and parameters. SparkConf provides configurations to run a Spark application.
Creating a SparkCOnf object with SparkConf(), which will load the values from spark. Java system properties as well.
Most commonly used attributes of SparkConf 
 - set(key, value) - to set a configuration property
 - setMaster(value) - to set the master URL
 - setAppName(value) - to set an application name
 - get(key, defaultValue=None) - to get a configuration value of a key
 - setSparkHome(value) - to set Spark installation path on worker nodes

The following code block has the lines, when they get added in the Python file, it sets the basic configurations for running a PySpark application.
```
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("PySpark App").setMaster("spark://master:7077")
sc = SparkContext(conf=conf)
```
**SparkFiles**

In Appache Spark, we can upload your files using sc.addFile (sc is default SparkContext) and get the path on a worker using SparkFiles.get. Thus, SparkFiles resolve the paths to files added through SparkContext.addFile().
SparkFiles contain the following classmethods:
 - get(filename)
 - getrootdirectory()
get(filename)
It specifies the path of the file that is added through SparkContext.addFile()
getrootdirectory()
It specifies the path to the root directory, which contains the file that is added through the SparkContext.addFile()

**StorageLevel**

StorageLevel decides how RDD should be stored. In Apache Spark, StorageLevel decides whether RDD should be stored in the memory or should it be stored over the disk, or both. It also decides whether to serialize RDD and whether to replicate RDD partitions.

Now, to decide the storage of RDD, there are different storage levels, which are given below

 - DISK_ONLY = StorageLevel(True, False, False, False, 1)
 - DISK_ONLY_2 = StorageLevel(True, False, False, False, 2)
 - MEMORY_AND_DISK = StorageLevel(True, True, False, False, 1)
 - MEMORY_AND_DISK_2 = StorageLevel(True, True, False, False, 2)
 - MEMORY_AND_DISK_SER = StorageLevel(True, True, False, False, 1)
 - MEMORY_AND_DISK_SER_2 = StorageLevel(True, True, False, False, 2)
 - MEMORY_ONLY = StorageLevel(False, True, False, False, 1)
 - MEMORY_ONLY_2 = StorageLevel(False, True, False, False, 2)
 - MEMORY_ONLY_SER = StorageLevel(False, True, False, False, 1)
 - MEMORY_ONLY_SER_2 = StorageLevel(False, True, False, False, 2)
 - OFF_HEAP = StorageLevel(True, True, True, False, 1)

**MLlib**

Apache Spark offers a Machine Learning API called MLlib. PySpark has this machine learning API in Python as well. It supports different kind of algorithms, which are mentioned below
 - mllib.classification − The spark.mllib package supports various methods for binary classification, multiclass classification and regression analysis. Some of the most popular algorithms in classification are Random Forest, Naive Bayes, Decision Tree, etc.
 - mllib.clustering − Clustering is an unsupervised learning problem, whereby you aim to group subsets of entities with one another based on some notion of similarity.
 - mllib.fpm − Frequent pattern matching is mining frequent items, itemsets, subsequences or other substructures that are usually among the first steps to analyze a large-scale dataset. This has been an active research topic in data mining for years.
 - mllib.linalg − MLlib utilities for linear algebra.
 - mllib.recommendation − Collaborative filtering is commonly used for recommender systems. These techniques aim to fill in the missing entries of a user item association matrix.
 - spark.mllib − It ¬currently supports model-based collaborative filtering, in which users and products are described by a small set of latent factors that can be used to predict missing entries. spark.mllib uses the Alternating Least Squares (ALS) algorithm to learn these latent factors.
- mllib.regression − Linear regression belongs to the family of regression algorithms. The goal of regression is to find relationships and dependencies between variables. The interface for working with linear regression models and model summaries is similar to the logistic regression case.

**Serializers**

Serialization is used for performance tuning on Apache Spark. All data that is sent over the network or written to the disk or persisted in the memory should be serialized. Serialization plays an important role in costly operations.

PySpark supports custom serializers for performance tuning. The following two serializers are supported by PySpark
*MarchalSerializer*
Serializes objects using Python’s Marshal Serializer. This serializer is faster than PickleSerializer, but supports fewer datatypes.
*PickleSerializer*
Serializes objects using Python’s Pickle Serializer. This serializer supports nearly any Python object, but may not be as fast as more specialized serializers.

**Jargon of Apache Spark**
**Job** : A piece of code which reads some input from HDFS or local, 
performs some computation on the data and writes some output data.

**Stages** : Jobs are divided into stages. Stages are classified as a Map or reduce stages.
Stages are divided based on computational boundaries, all computations (operators) cannot be Updated in a single Stage.
It happens over many stages.

**Tasks**: Each stage has some tasks, one task per partition. One task is executed on one partition
of data on one executer (machine).

**DAG**: DAG stands for Directed Acyclic Graph, in the present context its a DAG of operators.

**Executor**: The process responsible for executing a task

**Master**: The machine on which the Driver program runs

**Slave**: The machine on which the Executor program runs

**Spark Components**

1. Spark Driver
 - separate process to execute user applications
 - creates SparkContext to schedule jobs execution and negotiate with cluster manager
2. Executors 
 - run tasks scheduled by driver
 - store computation results in memory, on disk or off-heap
 - interact with storage systems
3. Cluster Manager
 - Mesos
 - YARN
 - Spark Standalone

 * SparkContext
	 – represents the connection to a Spark cluster, and can be used to create RDDs, 
	accumulators and broadcast variables on that cluster
 * DAGScheduler
	 - computes a DAG of stages for each job and submits them to TaskScheduler detemines preferred locations for tasks (based on cache status or shuffle files locations) and finds minimum schedule to run the jobs
 * TaskScheduler
	 – responsible for sending tasks to the cluster, running them, retrying if there are failures, and mitigating stragglers
 * SchedulerBackend
	 - backend interface for scheduling systems that allows plugging in different implemen-
	tations(Mesos, YARN, Standalone, local)
 * BlockManager
	 - provides interfaces for putting and retrieving blocks both locally and remotely into various stores (memory, disk, and off-heap)

**Architecture**

Spark has a small code base and the system is divided in various layers.

 - Spark creates a operator graph
 - When the user runs an action(like collect). The Graph is submitted to a DAG Scheduler.
 - DAG scheduler divides operator graph into (map and reduce) stages of tasks.
 - A stage is comprised of tasks based on patitions of the input data.
 - The DAG scheduler pipelines operators together to optimize the graph.
(For example Many map operators can be scheduled in a single stage). 
This optimization is key to Sparks perfomance. 
The final result of a DAG scheduler is a set of stages. The stages are passed on to the Task Scheduler. 
 - The task scheduler launches tasks via cluster manager.(Spark Standalone/Yarn/Mesos)
 - The task scheduler doesn't know abuot dependencies among stages.

**Operations**

* Transformations 
Transformations construct a new RDD from a previous one. For example, one common transformation is
filtering data that matches a predicate.

* Actions
Actions, on the other hand, compute a result based on an RDD, and either return it to the driver program or
save it to an external storage system (e.g., HDFS).



















