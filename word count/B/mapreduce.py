class MapReduce:

    def mapper(self, key, value):
        raise NotImplementedError

    def combiner(self, key, values):
        for value in values:
            yield(key, value)

    def reducer(self, key, values):
        raise NotImplementedError

    @staticmethod
    def aggregator(pairs):
        pairs = sorted(pairs)
        key, values = None, []
        for pair in pairs:
            k,v = pair
            if k != key:
                if len(values) > 0:
                    yield (key,values)
                key, values = k, []
            values.append(v)
        if len(values) > 0:
            yield (key,values)

    @classmethod
    def run(job_class, input):
        job_object = job_class()
        combined_pairs = []
        for line in input:

            mapped_pairs = []
            for pair in job_object.mapper(None,line):
                mapped_pairs.append(pair)
                #print "mapped pair",pair

            aggregated_pairs = []
            for key, values in MapReduce.aggregator(mapped_pairs):
                aggregated_pairs.append((key, values))
                #print "aggregated pair",(key,values)

            for key, values in aggregated_pairs:
                for pair in job_object.combiner(key, values):
                    combined_pairs.append(pair)
                    #print "combined pair",pair

        aggregated_pairs = []
        for key, values in MapReduce.aggregator(combined_pairs):
            aggregated_pairs.append((key, values))
            #print "aggregated pair",(key,values)

        reduced_pairs = []
        for key, values in aggregated_pairs:
            for pair in job_object.reducer(key, values):
                reduced_pairs.append(pair)
                #print "reduced pair",pair

        return reduced_pairs
