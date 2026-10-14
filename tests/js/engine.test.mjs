// Tests du moteur du parcours joueur (static/play/engine.js).
// Lancés par tests/test_play_engine.py : node --test tests/js/engine.test.mjs
import assert from "node:assert/strict";
import { test } from "node:test";

import { appraise, choose, createGame, startScene } from "../../static/play/engine.js";

function scenes(critical) {
    return [{
        scene_id: 1,
        title: "Scène",
        condition: null,
        entry_points: [],
        default_entry: "1",
        debriefs: [],
        parcours: [{ node_id: "C1_S1_I1", responses: [] }],
        id_to_parcours: {
            1: {
                node_id: "C1_S1_I1",
                responses: [
                    { idx: 0, next_id: "-1", Empathy: 3, critical: false },
                    { idx: 1, next_id: "-1", Empathy: 2, critical },
                ],
            },
        },
    }];
}

test("une réponse critique donne un bilan de scène « dur », quelle que soit la note", () => {
    const game = createGame(scenes(true));
    startScene(game);
    choose(game, game.current.responses[1], 450);
    assert.equal(game.sceneCritical, 1);
    assert.deepEqual(game.times, [450]);
    const verdict = appraise(game.sceneScores, 3, game);
    assert.equal(verdict.tone, "hard");
    assert.match(verdict.lead, /Une réponse critique/);
});

test("sans réponse critique, le bilan suit la note", () => {
    const game = createGame(scenes(false));
    startScene(game);
    choose(game, game.current.responses[1]);
    assert.deepEqual(game.times, [null]);
    assert.equal(appraise(game.sceneScores, 3, game).tone, "good");
});
