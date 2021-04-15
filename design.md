# Data model design

Below is a simplified version of my proposed models. It doesn't have every field in an actual real-world scenario but enough ones to explain the design choice.

seller:
- seller_id: uuid
- seller_payout_day: enum(mon, tue, wed, thur, fri)
- seller_payout_frequency_in_week: int
- seller_balance: float
- seller_payout_dates: varchar[]
	
product
- seller_fkid: uuid
- product_id: uuid
- product_title: varchar
- product_description: varchar
- product_price: float
- product_balance: float

purchase:
- product_fkid: uuid
- purchase_id: uuid
- purchase_type: enum(purchase, refund)
- purchase_discount_in_percent: float
- purchase_final_price: float
- purchase_buyer_email: varchar
- purchase_timestamp: timestamp

When a customer make a purchase or a refund:
- First update the purchase table with the corresponding type (whether it's a purchase or a refund), its discount rate in percent, its final price that the customer pay for, their email and its transaction timestamp.
- Second, update the product table by adding the final purchase price to the product balance or subtracting the final refund price.
- Lastly, update the seller table by recalculating the seller balance by summing all the product balances.

At the end of the day, a product balance is the balance for a particular product while seller balance is the total balance that one has across all of their products.

To support rolling payouts, depending on the payout frequency in week (whether it's every 1 week, every 2 weeks, and so on), on the payout day (whether it's Monday, Tuesday, and so on), query the purchase table to calculate the sum of those purchases prices which have the corresponding start and end date timestamps up to a week before that. For example,
- If it's 1-week payout, and the payout day is Friday 23th, the corresponding start and end timestamps are Monday 12th and Friday 16th.
- If it's 2-week payout, and the payout day is Friday 23th, the corresponding start and end timestamps are Monday 5th and Friday 16th.

The last step is to record these date ranges in the seller table by appending these in the `seller_payout_dates` column. This also helps if one wants to change the payout frequency rate or payout day in the future, one can validate again and make sure those upcoming payout dates don't overlap.

To make the database operations more performant, columns that can be indexed are:
- `seller_balance`
- `seller_payout_dates`
- `product_balance`
- `purchase_final_price`
- `purchase_timestamp`
