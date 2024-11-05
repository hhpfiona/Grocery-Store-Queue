if __name__ == '__main__':
    import coverage
    import pytest

    cov = coverage.Coverage(include=['container.py'])
    cov.start()

    pytest.main(["test_priority_queue.py"])

    cov.stop()
    cov.save()


    percent_covered = cov.html_report()

    print(f'Code coverage: {percent_covered :.2f}%')

    import webbrowser
    import os.path

    webbrowser.open(f'file://{os.path.dirname(__file__)}/htmlcov/index.html')
