func maxProfit(prices []int) int {
    min_price := prices[0]
    max_profit := 0

    for _ , price := range prices{
        if price < min_price{
            min_price = price
        }else {
            profit := price - min_price
            if profit > max_profit{
                max_profit = profit
            }
        }


    }
    return max_profit
}