from crew import TranslatorCrew


def run():
    """
    Run the Crew.
    """

    inputs = {
        "sentence": "내 이름은 임우현이야. 한때 프로게이머를 꿈꾸었지만, 지금은 머신러닝 소프트웨어 엔지니어가 되고자 공부하고 있어. 요즘에도 롤 프로게이머인 페이커 선수를 보면서 이전에 꿈꾸었던 것들에 대해서 조금이나마 미련도 있지만, 열정을 불태우고, 철저한 자기관리를 하며 해마다 정상의 자리를 지키는 페이커 선수의 모습을 보면서 미련보다는 내 인생을 살아가는데 있어서 많은 동기부여를 받는 것 같아. 그런 의미에서 과거의 꿈들은, 현재의 나를 만들었다는 생각이 들어."
    }

    TranslatorCrew().assemble_crew().kickoff(  # type: ignore
        inputs=inputs,
    )


if __name__ == "__main__":
    run()
