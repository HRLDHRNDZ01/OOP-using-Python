class Course:
    def __init__(self, title, instructor, lectures, price):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_ratings = 0

    def __str__(self):
        return f'{self.title} by {self.instructor}'

    def new_user_enrolled(self, user):
        self.users.append(user)

    def received_a_rating(self, new_rating):
        self.avg_ratings = (self.avg_ratings * self.ratings + new_rating) / (self.ratings + 1)
        self.ratings += 1

    def show_details(self):
        print("Course Title: ", self.title)
        print("Instructor: ", self.instructor)
        print("Price: ", self.price)
        print("Number of lectures: ", self.lectures)
        print("Users: ", self.users)
        print("Average ratings: ", self.avg_ratings)


class VideoCourse(Course):
    def __init__(self, title, instructor, lectures, price, length_video):
        super().__init__(title, instructor, lectures, price)
        self.length_video = length_video

    def show_details(self):
        super().show_details()
        print("Video Length: ", self.length_video)


class PdfCourse(Course):
    def __init__(self, title, instructor, lectures, price, pages):
        super().__init__(title, instructor, lectures, price)
        self.pages = pages

    def show_details(self):
        super().show_details()
        print("Pages: ", self.pages)


# Testing the corrected classes
vc = VideoCourse('Learn Python', 'Harold', 40, 50, 60)
vc.new_user_enrolled('Victor')
vc.new_user_enrolled('Rudy')
vc.new_user_enrolled('Chet')
vc.received_a_rating(60)
vc.received_a_rating(55)
vc.received_a_rating(58)
vc.show_details()

print()

pc = PdfCourse('Learn JavaScript', 'Zayn', 70, 90, 68)
pc.new_user_enrolled('Lebron')
pc.new_user_enrolled('Stephen')
pc.new_user_enrolled('Kevin')
pc.received_a_rating(76)
pc.received_a_rating(97)
pc.received_a_rating(89)
pc.show_details()
