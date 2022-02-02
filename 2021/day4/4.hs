import Data.List
import qualified Data.Text as T
import qualified Data.Text.IO as T

type Board = [[Int]]

part1 :: [Int] -> [Board] -> Int
part1 d bs =
  let 
    _isWinner xs  = any (all (`elem` xs))
    isWinner xs b = (_isWinner xs b) || (_isWinner xs $ transpose b)
    _winners      = map (\xs -> (xs, filter (isWinner xs) bs)) $ inits d
    winners       = filter ((/=[]) . snd) _winners
    (fd, fb)      = head winners
    lastDraw      = last fd
  in lastDraw * sum (filter (`notElem` fd) $ concat $ head fb)

main :: IO ()
main = do
  input <- T.splitOn (T.pack "\n\n") <$> T.readFile "input.txt"
  let draws  = map (strToInt . T.unpack) $ T.splitOn (T.pack ",") $ head input
  let boards = map (map T.unpack . T.splitOn (T.pack "\n")) $ tail input
  let bs     = map strToBoard boards

  print $ part1 draws bs
   
-- Parse helpers
strToInt :: String -> Int
strToInt = read :: String -> Int

strToBoard :: [String] -> Board
strToBoard = foldr f []
  where f s acc = (map (strToInt) $ words s) : acc

















