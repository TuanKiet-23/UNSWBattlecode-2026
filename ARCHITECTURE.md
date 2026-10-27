# BigHero – Bot Architecture & Strategy

## 1. Project Architecture

BigHero is a Python strategy bot designed to make autonomous decisions under partial visibility.

The bot follows a decision-making process that combines environmental observations, stored information, route evaluation and tactical action selection.

**Decision Flow**

Game Observation → State & Memory Update → Route and Threat Evaluation → Heuristic Scoring → Tactical Decision → Action

## 2. Environment Observation & Memory

The bot processes visible terrain, unit positions, movement history and available resources.

Because the entire environment is not always visible, it also uses stored information about previously explored areas and portal connections to support subsequent decisions.

## 3. Graph-Based Navigation

BigHero uses graph-based representations of accessible terrain to evaluate possible movement routes.

Navigation decisions consider:

- Accessible paths and potential obstacles
- Collision risks and dangerous positions
- Exploration opportunities
- Resource locations
- Available escape routes

## 4. Heuristic Decision-Making

Rather than following a fixed movement pattern, BigHero evaluates candidate actions using multiple factors.

Its heuristic approach balances survival, exploration, resource collection and tactical opportunities.

## 5. Adaptive Tactical Strategy

The bot adjusts its behaviour based on the current game state.

Key capabilities include:

- Enemy threat assessment
- Risk-aware movement
- Resource prioritisation
- Portal navigation
- Dynamic unit splitting
- Role-based tactical behaviour

## 6. Development & Validation

We developed multiple versions of BigHero, experimenting with different strategies and reviewing their behaviour through testing.

Our workflow involved replay analysis, debugging, targeted scenario checks and comparison against earlier strategies.

This process helped us identify weaknesses, evaluate alternative approaches and refine the bot's decision-making logic.

## 7. Technology & Attribution

**Language:** Python

**Approach:** Graph-based navigation, heuristic algorithms, stateful decision-making and iterative testing.

Development involved AI-assisted workflows. The official competition helper SDK and game engine are external components, separate from our strategy implementation.
