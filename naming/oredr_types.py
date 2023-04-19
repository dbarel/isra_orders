class OrderTypes:
    delivery = "משלוח"
    take_away = "איסוף עצמי"
    parking_delivery = "שירות משלוח לחניה - יום שישי החל מ 9:00"  # covid-19 take_away

    def is_delivery(self, order_type):
        if self.delivery in order_type:
            if self.parking_delivery != order_type:
                return True
        return False


second_holly_day_2023 = [
    "איסוף עצמי בערב שביעי של פסח יום שלישי - 11.04.23 בשעות - 12:00 - 08:00",
    "איסוף עצמי לשביעי של פסח ביום שני - 10.04.23 בשעות - 20:00 - 16:00",
    "משלוח למודיעין-מכבים-רעות לשביעי של פסח ביום שלישי - 11.04.23 בשעות 12:00 - 08:00",
    "משלוח למודיעין-מכבים-רעות לשביעי של פסח ביום שני - 10.04.23 בשעות 21:00 - 16:00"
]
