import Data.List
import qualified Data.Text as T
import qualified Data.Text.IO as T

strToInt :: String -> Int
strToInt = read :: String -> Int

part1 :: [Int] -> Int
part1 xs = sum $ map (\x -> abs(x - mid)) xs
  where
    mid = xs !! ((length xs) `div` 2)


part2 :: [(Int, Int)] -> Int
part2 xs = minimum dists
  where
      cost i (a, b) = let n = abs(i - a) in (n * (n + 1)) `div` 2 * b
      dist i = foldl (\acc pr -> acc + cost i pr) 0 xs
      dists  = map dist [0..fst $ last xs]

main :: IO ()
main = do
  input <- sort . map (strToInt . T.unpack) . T.splitOn (T.pack ",") <$> T.readFile "input.txt"
  let hist = map (\g -> (head g, length g)) $ group input
  
  print $ part1 input
  print $ part2 hist
 