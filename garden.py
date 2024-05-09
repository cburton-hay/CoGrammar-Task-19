# ======= Working with the spaCy ===== #
import spacy

nlp = spacy.load('en_core_web_md')

sentence_1 = "The old man the boat."
sentence_2 = "The complex houses married and single soldiers and their families."
sentence_3 = "Mary gave the child a Band-Aid."
sentence_4 = "That Jill never here hurts."
sentence_5 = "The cotton clothing is made of grows in Mississippi."

doc1 = nlp(sentence_1)
doc2 = nlp(sentence_2)
doc3 = nlp(sentence_3)
doc4 = nlp(sentence_4)
doc5 = nlp(sentence_5)

gardenpathSentences = [doc1, doc2, doc3, doc4, doc5]

for token in gardenpathSentences:
    print(token.doc)

# Tokenisation------------------------------------------------------------------

print([token.orth_ for token in doc1])
print([token.orth_ for token in doc2])
print([token.orth_ for token in doc3])
print([token.orth_ for token in doc4])
print([token.orth_ for token in doc5])


# Named entity recognition
# Get labels and entities and print them

print([(i, i.label_, i.label) for i in doc1.ents])
print([(i, i.label_, i.label) for i in doc2.ents])
print([(i, i.label_, i.label) for i in doc3.ents])
print([(i, i.label_, i.label) for i in doc4.ents])
print([(i, i.label_, i.label) for i in doc5.ents])


# Get an explanation of an entity and print it
entity_person = spacy.explain("PERSON")
print(f"PERSON:{entity_person}")
# OUTPUT = PERSON:People, including fictional
# "Mary" and "Jill" were labelled as PERSON which makes sense in the context.

entity_GPE = spacy.explain("GPE")
print(f"GPE:{entity_GPE}")
# OUTPUT = GPE:Countries, cities, states
# "Mississippi" was labelled as GPE which makes sense as it's a state in USA.

entity_ORG = spacy.explain("ORG")
print(f"ORG:{entity_ORG}")
# ORG:Companies, agencies, institutions, etc.
# "Band-Aid" was labelled as ORG which makes sense as it's brand of plasters.