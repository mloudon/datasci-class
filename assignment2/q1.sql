select  term
 from frequency 
 where docid="10398_txt_earn" and count=1
 union
 select term
 from frequency 
 where docid="925_txt_trade" and count=1
 
 
 select count (distinct docid)
 from frequency
 where term like "parliament"
 
 select docid, count (term)
 from frequency
 group by docid
 having sum(count)>300
 
 select docid
 from frequency
 where  term like"world"
 intersect
 select docid
 from frequency
 where term like "transaction"
 
 --(2,3) is each element in row 2 of a * each element in col 3 of b
 -- so in a, (2,1) by in b, (1,3)
 select a.row_num, a.col_num, a.value, b.row_num, b.col_num, b.value 
 from a
inner join b
 on (a.col_num=b.row_num)
 where a.row_num=2
 and b.col_num=3
 
 select sum(a.value*b.value)
 from a
inner join b
 on (a.col_num=b.row_num)
 where a.row_num=2
 and b.col_num=3
 
 
 select sum(a.count*b.count)
 from frequency as a
inner join frequency as b
 on (a.term=b.term)
 where a. docid='10080_txt_crude' and  b.docid='17035_txt_earn'
 
select a.docid, b. term, sum(a.count*b.count)
from frequency as a, frequency as b
where (a.term=b.term) 
 and a. docid='10080_txt_crude' and  b.docid='17035_txt_earn'
group by a.docid, b.docid
 
 
 create table freq2 as
 SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count

 select a.docid, b. term, sum(a.count*b.count)
 from freq2 as a, freq2 as b
where (a.term=b.term) and b. docid='q'
group by a.docid, b.docid
order by  sum(a.count*b.count) desc