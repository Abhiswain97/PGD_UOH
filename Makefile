CC = clang

.PHONY = run

all: run 

run: 
	${CC} tfidf.cpp -o tfidf.exe
	tfidf.exe
