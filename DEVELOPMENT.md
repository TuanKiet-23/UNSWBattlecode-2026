# BigHero – Development & Iteration

## Overview

BigHero was developed through multiple iterations during UNSW Battlecode 2026. Our focus was not simply to make the bot execute valid actions, but to improve how it evaluated risks, explored the environment and responded to changing game conditions.

Working in a two-person team, we experimented with different Python strategies, reviewed gameplay behaviour and used testing results to guide further changes.

## 1. Building the Foundation

The early versions focused on establishing reliable movement and decision-making.

Key areas included:
- Representing accessible terrain for navigation.
- Identifying obstacles and potential collisions.
- Evaluating available movement directions.
- Balancing exploration with immediate survival.

These components provided a foundation for more complex tactical decisions.

## 2. Exploring Alternative Strategies

As the project evolved, we experimented with different approaches to improve the bot's behaviour.

Our development archive includes experiments involving:
- Enemy threat assessment and sprint-related risks.
- Portal navigation and escape scenarios.
- Dynamic unit splitting and survival decisions.
- Resource collection and map exploration.
- Route evaluation and avoidance of confined areas.

Not every experimental strategy was retained. We reviewed unsuccessful approaches rather than assuming that additional complexity would always improve performance.

## 3. Improving Decision-Making

Later development focused on combining navigation, environmental memory and tactical evaluation.

Instead of making decisions based on a single factor, the bot considered multiple conditions before selecting an action.

These included accessible space, opponent threats, resource opportunities, remembered terrain and the current state of its units.

This required balancing competing objectives, particularly survival, exploration and resource collection.

## 4. Testing and Debugging

Testing was an important part of our development process.

We used:
- Recorded game replays to inspect unexpected behaviour.
- Controlled comparisons between strategy variants.
- Targeted scenarios to investigate specific tactical problems.
- Python scripts to audit decision-making components.
- Regression checks to identify behaviour affected by code changes.

We also reviewed execution constraints to ensure that strategy improvements remained practical within the competition environment.

## 5. BigHero V8 Merit

V8 Merit represents one of the later versions of our Python strategy bot.

This version brings together navigation, persistent environmental information, risk assessment and adaptive tactical behaviour.

The project also includes supporting scripts and archived test records used during development and validation.

## 6. Lessons Learned

The competition reinforced several lessons:

**Reliable behaviour matters.** A strategy must handle difficult scenarios, not just perform well in favourable situations.

**More complex logic is not always better.** New features need to be evaluated against existing approaches.

**Testing supports better decisions.** Replay analysis and controlled comparisons help distinguish useful improvements from assumptions.

**Iteration is part of engineering.** Debugging, revising and occasionally rejecting an approach are important steps in developing a reliable solution.

## 7. Development Approach

The project combined Python programming, algorithmic problem-solving, experimentation, testing and AI-assisted development.

The official Battlecode SDK and game engine were external tools used to support development.

Our archived versions, experiment records and validation scripts document the technical work carried out during the competition.
