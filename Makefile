
all: test merge

tests: libs games

libs: cglogger 

cglogger: 
	cd libs/cglogger  && \
	python3 -m pytest tests

games: spring_challenge_2022

spring_challenge_2022: 
	cd game/spring_challenge_2022 && \
	python3 -m pytest tests

merge: merge_spring_challenge_2022

merge_spring_challenge_2022:
	mkdir -p target
	./tools/merger.sh -l cglogger -o ./target spring_challenge_2022