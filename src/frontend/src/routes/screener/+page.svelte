<script>
    let minAmountFrom = "";
    let minAmountTo = "";
  
    function filterStrategies() {
      alert(`Фильтр будет применен с параметрами: от ${minAmountFrom || 0} до ${minAmountTo || "100"}`);
      window.location.href = '/menu';
    }
  </script>
  
  <style>
    :global(body) {
      font-family: Arial, sans-serif;
      background-color: #121212;
      color: #FFFFFF;
      margin: 0;
      padding: 0;
    }
  
    .header {
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
      background-color: #1F1F1F;
    }
  
    .search-bar {
      width: 50%;
      padding: 10px;
      border: none;
      border-radius: 8px;
      margin-right: 10px;
      font-size: 16px;
    }
  
    .search-button {
      padding: 10px 20px;
      border: none;
      background-color: #b1f5ec;
      color: #121212;
      border-radius: 8px;
      font-size: 16px;
      cursor: pointer;
      border: 2px solid #7daea7e0;
    }
  
    .filters {
      padding: 20px;
      display: flex;
      justify-content: space-around;
      background-color: #1F1F1F;
      border-bottom: 1px solid #b1f5ec;
    }
  
    .filter-group {
      display: flex;
      flex-direction: column;
    }
  
    .filter-input1 {
      margin-top: 5px;
      padding: 5px;
      border: none;
      border-radius: 4px;
      font-size: 14px;
      color: #121212;
    }

    .filter-input2 {
      margin-top: 5px;
      padding: 5px;
      border: none;
      border-radius: 4px;
      font-size: 14px;
      color: #121212;
    }
  
    .filter-button {
      margin-top: 10px;
      padding: 10px;
      border: none;
      background-color: #b1f5ec;
      color: #121212;
      border-radius: 8px;
      font-size: 16px;
      cursor: pointer;
      border: 2px solid #7daea7e0;
      text-align: center;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  
    .strategy-cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      padding: 20px;
    }
  
    .strategy-card {
      background-color: #1F1F1F;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
      border: 1px solid #b1f5ec;
    }
  
    .strategy-card h3 {
      color: #b1f5ec;
      margin-bottom: 10px;
    }
  
    .footer {
      text-align: center;
      padding: 20px;
      background-color: #1F1F1F;
      border-top: 1px solid #b1f5ec;
    }
  </style>
  
  <header class="header">
    <input type="text" class="search-bar" placeholder="Введите название стратегии или имя автора" />
    <button class="search-button">🔍</button>
  </header>
  
  <main>
    <section class="filters">
      <div class="filter-group">
        <span>Вложение, $</span>
        <input
          type="number"
          placeholder="Сумма"
          class="filter-input1"
          bind:value={minAmountFrom}
        />
      </div>
      <div class="filter-group">
        <span>Максимальная просадка, %</span>
        <input
          type="number"
          placeholder="до 100"
          class="filter-input2"
          bind:value={minAmountTo}
        />
      </div>
      <button class="filter-button" on:click={filterStrategies}>Подобрать</button>
    </section>
  
    <section class="strategy-cards">
      <div class="strategy-card">
        <h3>Anti-mainstream 1</h3>
        <p>Подписчики: 25</p>
        <p>Минимальная сумма: $500</p>
        <p>Среднегодовая доходность: 22.5%</p>
        <p>Прогнозируемая просадка: -15%</p>
      </div>
      <div class="strategy-card">
        <h3>Anti-mainstream 2</h3>
        <p>Подписчики: 12</p>
        <p>Минимальная сумма: $100</p>
        <p>Среднегодовая доходность: 20.3%</p>
        <p>Прогнозируемая просадка: -10%</p>
      </div>
    </section>
  </main>
  
  <footer class="footer">
    <p>© 2025 MoneyButtonAI</p>
  </footer>
  