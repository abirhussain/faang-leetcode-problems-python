class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Solution Steps
        # 1. create event for both birth year and death year
        # 2. sort events by year, prioritizing births over deaths in case of a tie
        # 3. iterate through the events to find the year with the maximum population year
        # 4. return maximum population year

        # Step1:
        events = []
        for birth, death in logs:
            events.append((birth,1))
            events.append((death, -1))

        # Step2:
        events.sort(key=lambda x: (x[0],x[1]))

        # Step3:
        current_population = 0
        max_population = 0
        max_year = 1950

        for year, population in events:
            current_population += population
            if current_population > max_population:
                max_population = current_population
                max_year = year

        # Step4:
        return max_year
        
        ############### Complexity #######################
        # Time Complexity: O(n log n) where n is the number of events (twice the number of logs). Sorting the events dominates the time complexity.
        # Space Complexity: O(n) for storing the events.
