from django.db import models
from django.utils import timezone

class NumbersCalculation(models.Model):
    input_a = models.IntegerField()
    input_b = models.IntegerField()
    input_c = models.IntegerField()
    input_d = models.IntegerField()
    input_e = models.IntegerField()

    original_list = models.JSONField()
    sorted_list = models.JSONField()
    negative_values = models.JSONField()
    positive_count = models.IntegerField()
    even_count = models.IntegerField()
    odd_count = models.IntegerField()
    greater_than_ten = models.JSONField()
    average = models.FloatField()
    average_gt_50 = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        inputs = [self.input_a, self.input_b, self.input_c, self.input_d, self.input_e]
        return (
            f"Calculation {self.id}:\n"
            f"  Inputs: {inputs}\n"
            f"  Average: {self.average} (>50: {'Yes' if self.average_gt_50 else 'No'})\n"
            f"  Positives: {self.positive_count}, Negatives: {len(self.negative_values)}\n"
            f"  Even: {self.even_count}, Odd: {self.odd_count}\n"
            f"  >10: {self.greater_than_ten}"
        )
