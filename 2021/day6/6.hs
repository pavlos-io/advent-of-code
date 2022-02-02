import Data.List
import qualified Data.Map as M
import qualified Data.Text as T
import qualified Data.Text.IO as T

type Hist = M.Map Int Int

strToInt :: String -> Int
strToInt = read :: String -> Int

step :: Hist -> Hist
step hist =
  let 
    get key = M.findWithDefault 0 key hist
    grown   = M.fromList $ (\i -> (i - 1, get i)) <$> [1..8]
    born    = M.fromList [(6, get 0), (8, get 0)]
  in M.unionWith (+) grown born

nthGenCount :: Int -> Hist -> Int
nthGenCount n hist = sum . map (snd) $ M.toList nthGen
  where nthGen = last $ take n $ iterate step hist

main :: IO ()
main = do
  input <- sort . map (strToInt . T.unpack) . T.splitOn (T.pack ",") <$> T.readFile "input.txt"
  let _hist = map (\g -> (head g, length g)) $ group input
  let hist  = M.fromList _hist
  
  print $ nthGenCount 81 hist  -- pt1
  print $ nthGenCount 257 hist -- pt2
