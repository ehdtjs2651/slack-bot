import unittest
from unittest import TestSuite

from settings import IS_TEST_ALL


def run_tests():
    if IS_TEST_ALL:
        # 테스트 코드 탐색
        loader = unittest.TestLoader()
        # main 이 실행되는 폴더에서 탐색
        tests = loader.discover('.')
        # 테스트 실행
        testRunner = unittest.runner.TextTestRunner()
        testRunner.run(tests)

    # 특정 테스트 코드만 실행
    else:
        # 테스트 코드 그룹 추가
        fast = TestSuite()
        # 테스트 코드 추기
        # fast.addTest(EquipmentsInfoTest('test_CRUD_one'))

        # 테스트 실행
        runner = unittest.TextTestRunner()
        runner.run(fast)

