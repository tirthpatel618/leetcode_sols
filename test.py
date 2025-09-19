class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.cuisines = {}
        self.food_ratings = {}

        for i in range(len(foods)):
            self.food_ratings[foods[i]] = ratings[i]
            if cuisines[i] not in self.cuisines:
                self.cuisines[cuisines[i]] = []
            self.cuisines[cuisines[i]].append((foods[i]))
        
    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        self.food_ratings[food] = newRating


    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        highest_rated_food = ""
        highest_rating = -1

        for food in self.cuisines[cuisine]:
            rating = self.food_ratings[food]
            if rating > highest_rating or (rating == highest_rating and food < highest_rated_food):
                highest_rated_food = food
                highest_rating = rating
        
        return highest_rated_food
    

foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]
obj = FoodRatings(foods, cuisines, ratings)
obj.printrating()
