import Data.List
import qualified Data.Text as T
import qualified Data.Text.IO as T
-- part1 :: [In] -> [Int]

strToInt :: String -> Int
strToInt = read :: String -> Int

unpackToInt :: T.Text -> Int
unpackToInt = strToInt . T.unpack

main :: IO ()
main = do
  input <- T.lines <$> T.readFile "input.txt"
  let mkPt = (\[a, b] -> (unpackToInt a, unpackToInt b)) . T.splitOn (T.pack ",")
  let pts = map (sort . map (mkPt) . T.splitOn (T.pack " -> ")) input
  let nonDiag = filter (\[(x1,y1), (x2,y2)] -> x1 == x2 || y1 == y2) pts
  
  print $ nonDiag 