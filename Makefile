
all: tests merge

tests: libs games

libs: cglogger 

cglogger: 
	cd libs/cglogger  && \
	python3 -m pytest -s tests --cov=src

games: spring_challenge_2022 winter_shallenger_2022 spring_challenge_2023

spring_challenge_2022: 
	cd game/spring_challenge_2022 && \
	python3 -m pytest -s tests --cov=src

winter_shallenger_2023: 
	cd game/winter_shallenger_2023 && \
	python3 -m pytest -s tests --cov=src

spring_challenge_2023: 
	cd game/spring_challenge_2023

merge: merge_spring_challenge_2023

merge_spring_challenge_2022: spring_challenge_2022
	mkdir -p target
	./tools/merger.sh -l cglogger -o ./target spring_challenge_2022

merge_winter_shallenger_2022: winter_shallenger_2022
	mkdir -p target
	./tools/merger.sh -l cglogger -o ./target winter_shallenger_2022

merge_spring_challenge_2023: spring_challenge_2023
	mkdir -p target
	./tools/merger.sh -l cglogger -o ./target spring_challenge_2023
