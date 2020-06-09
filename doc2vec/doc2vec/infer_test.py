#python example to infer document vectors from trained doc2vec model
import gensim.models as g
from functools import reduce
import codecs

#parameters
model="toy_data/model.bin"
test_docs="toy_data/test_docs.txt"
output_file="toy_data/test_vectors.txt"

#inference hyper-parameters
start_alpha=0.01
infer_epoch=1000

#load model
m = g.Doc2Vec.load(model)
test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines() ]
test_docs = reduce(list.__add__,test_docs)

print('分词后的sql为:',test_docs[:])
print('分词后的sql为:',len(test_docs))
# #infer test vectors
with open(output_file, "w+") as f:
    for d in test_docs:
        f.write( " ".join([str(x) for x in m.infer_vector(doc_words=[d], alpha=start_alpha, steps=infer_epoch)]) + "\n" )
# output.flush()
# output.close()
