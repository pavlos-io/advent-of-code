import Data.Char

data Dir = Horz | Vert 
  deriving (Show)

data In = In Dir Int 
  deriving (Show)


getIns :: [String] -> [In]
getIns = map (parse . words)
  where parse ("forward":val:[]) = In Horz (digitToInt $ head val)
        parse ("down":val:[])    = In Vert (digitToInt $ head val)
        parse ("up":val:[])      = In Vert (negate $ digitToInt $ head val)

part1 :: [In] -> [Int]
part1 = foldl updState [0, 0]
  where updState (x:y:[]) (In Horz v) = [x + v, y]
        updState (x:y:[]) (In Vert v) = [x, y + v]

part2 :: [In] -> [Int]
part2 = foldl updState [0, 0, 0]
  where updState (x:y:aim:[]) (In Horz v) = [x + v, y + v * aim, aim]
        updState (x:y:aim:[]) (In Vert v) = [x, y, aim + v]

main :: IO ()
main = do
  input <- getIns . lines <$> readFile "input.txt"
  
  print $ product $ part1 input
  print $ product $ take 2 $ part2 input