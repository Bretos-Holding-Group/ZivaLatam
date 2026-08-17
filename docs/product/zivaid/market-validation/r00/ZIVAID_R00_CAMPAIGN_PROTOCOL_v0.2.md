# ZivaID R00 — Neutral Verification Campaign Protocol v0.2

**Status:** Controlled amendment — pre-execution
**Working public title:** ¿Cuánto de tu identidad tienes que repetir?
**Internal name:** Campaña ZivaID
**Budget:** CLP $0 paid acquisition
**Instrument ID:** `R00-INSTR-v0.2`
**Concept ID:** `CONCEPT-R00-v0.2`

## 1. Purpose

This campaign is a research instrument, not a product launch. Its purpose is to discover whether people repeatedly experience identity/document verification friction and what consequences follow.

The public-facing campaign must not begin by explaining ZivaID. The participant must have an opportunity to describe the problem without solution priming.

## 2. Campaign architecture

```text
Neutral prompt
   ↓
Organic response / street approach
   ↓
Discovery question
   ↓
Recent concrete example
   ↓
Frequency + consequence
   ↓
Evidence registration
   ↓
Optional concept test
   ↓
Follow-up behavior
```

## 3. Public-facing creative rule

The first exposure may use only the neutral research question and a request to share experience. It must not claim:

- that ZivaID already exists;
- that the problem is proven;
- that a particular technology solves it;
- that a government or company endorses the research;
- that the participant is expected to buy anything.

## 4. Organic social experiment

Use the same core prompt across Instagram, Facebook and TikTok during the first controlled wave so that differences in wording do not become an uncontrolled variable.

### Core prompt

> **¿Cuánto de tu identidad tienes que repetir?**
>
> Cuéntanos: ¿cuándo fue la última vez que un trámite o servicio te pidió demostrar información o entregar documentos que ya habías presentado antes?

The call to action should request an experience, not a yes/no endorsement of ZivaID.

### Comment handling

Classify public responses into:

- concrete recent experience;
- vague agreement;
- no experience / contradiction;
- unrelated;
- recruitment opportunity.

Do not count likes, views or shares as problem evidence. They are distribution metrics only.

## 5. Street campaign

Use the same discovery sequence as the interview protocol. The first objective is to learn what the person actually experienced, not to persuade them.

Suggested approach:

> Hola. Estoy haciendo una investigación breve sobre cómo las personas demuestran información y documentos para hacer trámites. No estoy vendiendo nada. ¿Te puedo hacer unas preguntas? Son unos cinco minutos.

Stop immediately when the person declines.

## 6. Two-stage questioning

### Stage A — Blind discovery

ZivaID is not named.

1. ¿Qué tipos de trámites o servicios has tenido que hacer durante el último año donde te pidieron demostrar información sobre ti?
2. Piensa en el último de esos trámites. ¿Qué información o documentos te pidieron?
3. ¿Habías entregado alguno de esos datos o documentos antes en otro proceso?
4. ¿Qué pasó exactamente?
5. ¿Cuántas veces te ha ocurrido algo parecido?
6. ¿Qué consecuencia tuvo la última vez?
7. ¿Cuánto tiempo, dinero o esfuerzo adicional te tomó?
8. ¿Qué hiciste para resolverlo?
9. ¿Qué haces hoy para evitar que vuelva a pasar?
10. Si pudieras cambiar una sola parte de ese proceso, ¿cuál cambiarías?

### Stage B — Neutral concept test

Only after Stage A is complete:

> Imagina un sistema que permitiera demostrar que una determinada información es válida, pero que cada servicio pudiera verificar solamente lo necesario para su propio propósito. Por ejemplo, un servicio podría comprobar que cumples un requisito sin recibir automáticamente toda la información relacionada contigo.

Then ask:

1. ¿Qué problema resolvería esto, si alguno?
2. ¿En qué situación concreta lo usarías?
3. ¿Qué sería lo primero que te preocuparía?
4. ¿Qué tendría que demostrar el sistema para que confiaras en él?
5. ¿Qué información o usos no aceptarías?
6. Comparado con tu proceso actual, ¿qué tendría que ser mejor para que valiera la pena cambiar?
7. ¿Lo probarías en un piloto gratuito? ¿Por qué?
8. ¿Harías algo concreto ahora para participar en una prueba futura?

The researcher must record the answer before interpreting it.

## 7. Campaign variables

Freeze these variables for the first wave:

- public question;
- discovery sequence;
- concept description;
- evidence categories;
- severity scale;
- participant ID format;
- source channel labels.

Each interaction record must store `instrument_id`, `concept_id` (or `not_exposed`) and `wave_id`.

The first controlled wave is frozen as:

- `wave_id`: `R00-W01`
- `instrument_id`: `R00-INSTR-v0.2`
- `concept_id`: `CONCEPT-R00-v0.2`

A later wave may use a new instrument/version only through a traceable amendment.

### Required deviation log

Every researcher must record protocol deviations as they occur:

- deviation ID;
- participant ID or interaction ID;
- timestamp/date band;
- exact step/question affected;
- what actually happened;
- reason;
- whether the deviation occurred before or after concept exposure;
- impact on comparability;
- disposition: usable / quarantine / excluded.

A researcher may not silently improvise a changed question and treat the result as equivalent to a controlled interaction.

### Version integrity

Before each wave, the coordinator must archive the exact instrument and concept text used. The archive must contain the version identifier and content hash where technically available. The evidence register must point to that version.

The objective is reproducibility: a reviewer must be able to determine exactly which research instrument produced each evidence record.

Variables that may change only through amendment:

- target segment quotas;
- wording of core questions;
- decision thresholds;
- definition of usable evidence;
- concept description.

## 8. Distribution metrics vs research metrics

**Distribution metrics:** views, reach, comments, shares, saves, profile visits.

**Research metrics:** usable interactions, concrete incidents, frequency, consequence, severity, current workaround, contradictory evidence, concept reaction, behavioral commitment.

Distribution metrics must never be substituted for research evidence.

## 9. Campaign stop conditions

Pause the current wave if:

- the public prompt is repeatedly misunderstood;
- researchers are leading participants toward the desired answer;
- evidence cannot be linked to a participant/source record;
- sensitive data begins to accumulate;
- a channel produces systematically different results because of an uncontrolled wording or recruitment change.

A pause is a quality control action, not a failure.

## 10. Campaign output

Each wave must produce:

1. channel exposure summary;
2. recruitment counts;
3. completed discovery interactions;
4. usable evidence count;
5. problem/no-problem/unclear distribution;
6. top recurring use cases;
7. strongest contradictory findings;
8. concept-test reactions separated from discovery findings;
9. behavioral signals;
10. sampling limitations;
11. protocol deviation summary;
12. recommended amendment, continuation or stop decision.

## 11. Privacy boundary

Do not request or publish RUTs, passport numbers, identity documents, medical records, financial account data, migration case information, passwords, authentication codes or other sensitive source records.

If a participant voluntarily supplies such information, redirect the conversation to the process and do not copy the source material into the research register.
