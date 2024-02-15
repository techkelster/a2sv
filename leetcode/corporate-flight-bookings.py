class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookingsPre = [0] * (n + 2)
        ans = [0] * (n + 1)
        for i in range(len(bookings)):
            bookingsPre[bookings[i][0]] += bookings[i][2]
            bookingsPre[bookings[i][1] + 1] -= bookings[i][2]
        for i in range(1, len(bookingsPre) - 1):
            ans[i] = ans[i - 1] + bookingsPre[i]
        return ans[1:]
