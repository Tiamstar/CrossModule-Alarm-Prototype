def get_divisor(x: int) -> int:
# 问题：当 x == 0 时返回 0，导致下游模块可能出现除零错误
  if x > 0:
   return 2
  else:
   return 0 # <- 潜在问题：返回0将导致后续除法出错