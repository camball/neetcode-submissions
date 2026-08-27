class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Build running prefix and suffix products in one pass
        prefix_prod = 1
        suffix_prod = 1
        prefix_products = [1]
        suffix_products = [1]
        for num_l, num_r in zip(nums, nums[::-1]):
            prefix_prod *= num_l
            suffix_prod *= num_r
            prefix_products.append(prefix_prod)
            suffix_products.append(suffix_prod)

        # Padding arrays makes edge cases easier
        prefix_products.append(1)
        suffix_products.append(1)

        # Compute output array
        products = []
        for i in range(len(nums)):
            products.append(prefix_products[i] * suffix_products[len(suffix_products) - i - 3])

        return products
