from operator import ge
from simpleruleengine.token.SimpleToken import SimpleToken
from simpleruleengine.operator.NumericOperator import NumericOperator


class NumericToken(SimpleToken):
    def __init__(self, token_name: str, operator: NumericOperator):
        super().__init__(token_name, operator)

    def evaluate(self, value_to_evaluate):
        return self.operator.evaluate(value_to_evaluate)