prices = [1000, 1300, 1150, 850, 1150, 950, 1200, 1400, 1000, 600, 950, 700, 1170 , 750]

function maxprofile(prices) {
  let lucro = 0;
  let venda = prices[0];

  for (let i = 0; i < prices.length; i += 1) {
    // Math.min: Retorna a menor das duas expressões numéricas fornecidas.
    venda = Math.min(venda, prices[i]);
    // console.log(venda);  // 1-1000|2-1000|3-1000|4-850|5-850|6-850, 850, 850, 850, 600, 600, 600, 600, 600
    // Math.max: Retorna a maior das duas expressões numéricas fornecidas
    lucro = Math.max(lucro, prices[i] - venda);
    // console.log(lucro); // 1-0|2-300|3-300,4-300,|5-300|6-300, 350, 550, 550, 550, 550, 550, 570, 570
  }
  // console.log(lucro); // 570
  return lucro;
}
maxprofile(prices);
// console.log(maxprofile(prices)) // 570
